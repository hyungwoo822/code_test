import torch
import torch.nn as nn
from torchdiffeq import odeint
import matplotlib.pyplot as plt

# ── 1. Velocity 네트워크 정의 ──
class VelocityNet(nn.Module):
    def __init__(self, dim, hidden_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim + 1, hidden_dim),  # +1 for time t
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, dim),
        )

    def forward(self, x, t):
        # x: [B, dim], t: [B,1] or scalar
        t_feat = t.expand(x.size(0), 1)
        inp = torch.cat([x, t_feat], dim=1)
        return self.net(inp)  # velocity vector u_t(x)

# ── 2. Training loop (Conditional Flow Matching) ──
def train_rectified_flow(model, data_loader, optimizer, p_init_sampler, device):
    model.train()
    mse = nn.MSELoss()
    for batch in data_loader:                   # x0 ~ p_data
        x0 = batch[0].to(device)   
        x1 = p_init_sampler(x0.shape).to(device)  # x1 ~ p_init (e.g. Gaussian)
        t = torch.rand(x0.size(0), 1, device=device)  # t ~ Uniform[0,1]

        # 선형 보간에 해당하는 중간점 x_t
        x_t = (1 - t) * x0 + t * x1
        # target velocity = dx_t/dt = x1 - x0
        v_target = x1 - x0

        # 예측된 velocity
        v_pred = model(x_t, t)

        loss = mse(v_pred, v_target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# ── 3. Sampling (ODE integration) ──
def sample_rectified_flow(model, p_init_sampler, device, num_samples=64, dim=2, steps=100):
    model.eval()
    with torch.no_grad():
        # 초기 z ~ p_init
        z0 = p_init_sampler((num_samples, dim)).to(device)

        # ODE right-hand side: dx/dt = -u_t(x)  (backward 통합)
        def ode_rhs(t, x_flat):
            x = x_flat.view(num_samples, dim)
            t_tensor = torch.full((num_samples,1), float(t), device=device)
            v = model(x, t_tensor)
            return (-v).view(-1)

        # 0→1로 integrate
        ts = torch.linspace(0., 1., steps, device=device)
        z_t = odeint(ode_rhs, z0.view(-1), ts, method='rk4')
        x1 = z_t[-1].view(num_samples, dim)  # 최종 샘플
        return x1

# ── 4. 사용 예시 ──
if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # 예: 2D Gaussian → target 분포 (ring)
    def p_init_sampler(shape):
        return torch.randn(shape) * 1.5

    # 예제용 데이터 (ring)
    def ring_data_sampler(batch_shape):
        theta = torch.rand(batch_shape[0]) * 2 * torch.pi
        r = 3.0 + 0.3 * torch.randn(batch_shape[0])
        return torch.stack([r*torch.cos(theta), r*torch.sin(theta)], dim=1)

    # 데이터로더
    real_data = ring_data_sampler((500,))
    ds = torch.utils.data.TensorDataset(ring_data_sampler((10000,)))
    dl = torch.utils.data.DataLoader(ds, batch_size=128, shuffle=True)

    # 모델 & 옵티마이저
    model = VelocityNet(dim=2, hidden_dim=128).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    plt.figure(figsize=(5,5))
    plt.scatter(real_data[:,0].cpu(), real_data[:,1].cpu(), s=8, alpha=0.7)
    plt.title("Real Ring Data (Target)")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("real_data.png")
    plt.close()

    # 학습
    for epoch in range(1000):
        if epoch % 100 == 0:
            print(f" EPOCH : {epoch}")
        train_rectified_flow(model, dl, opt, p_init_sampler, device)

    # 샘플링
    samples = sample_rectified_flow(model, p_init_sampler, device, num_samples=500, dim=2)
    plt.figure(figsize=(5,5))
    plt.scatter(samples[:,0].cpu(), samples[:,1].cpu(), s=8, alpha=0.7, c="tab:blue", label="Generated")
    plt.title("Generated Samples (Rectified Flow)")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("generated_samples.png")
    plt.close()

    print("Generated samples shape:", samples.shape)
