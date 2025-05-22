import time
# fibonacci recur
def fibo_recur(x):
    if x == 1 or x == 2:
        return 1
    else :
        return fibo_recur(x-1) + fibo_recur(x-2)
start_time = time.time()
print(fibo_recur(40))
elapsed_time = time.time() - start_time
print(elapsed_time)

# fibonacci iter
d = [0] * 10001
def fibo_iter(x):
    d[0], d[1], d[2] = 0, 1, 1
    for i in range(3, x+1, 1):
        d[i] = d[i-1] + d[i-2]
    print(d[x])
start_time = time.time()
fibo_iter(40)
elapsed_time = time.time() - start_time
print(elapsed_time)

# Make 1
x = int(input())
d = [0] * 1001
d[1], d[2] = 0, 1
for i in range(3, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    
print(d[x])

# Ant warrior
x = int(input())
array = list(map(int, input().split()))
d = [0] * 100

for i in range(1, x+1):
    if i == 1:
        d[i] = array[0]
        continue
    d[i] = max(d[i-1], d[i-2] + array[i-1])
print(d[x])
'''
다른 코드들 에서는 
d[0] 부터 코드를 시작해서
d[0], d[1]에 대해서 선언을 해주어야지 max(d[i-1], d[i-2]) 부분에서 오류가 안났음 (i-2) index 오류 때문에 
하지만 우리는 1번째 칸부터 실행해서 괜찮음
'''


# Tile optimization
x = int(input())
d = [0] * 10001
d[0], d[1], d[2], d[3] = 0, 1, 3, 5
for i in range(4, x+1):
    d[i] = 2 * d[i-2] + d[i-1]
print(d[x])

# Efficient currency construction
x, total = map(int, input().split())
data = []
for i in range(x):
    data.append(int(input()))
d = [10001] * 10001
d[0] = 0
for i in data:
    d[i] = 1
for i in range(total+1):
    for currency in data:
        if d[i-currency] != 10001:
            # 여기서 min(d[i-currency]+1, d[i]) 안하고 d[i-currency]+1로 하면
            # [1, 3, 4] / total = 6 일때 오류 발생
            d[i] = min(d[i-currency]+1, d[i])
if d[total] == 10001:
    print(-1)
else :
    print(d[total])
