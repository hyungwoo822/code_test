graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9
# DFS
# recursively + stack
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')
    v = start
    for i in graph[v]:
        if not visited[i] :
            dfs(graph, i, visited)

dfs(graph, 1, visited)

# BFS
# queue
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

# Frozen Soda
from collections import deque
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False
def bfs(x, y):
    if data[x][y] == 1:
        return False
    queue = deque()
    queue.append((x,y))
    data[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                data[nx][ny] = 1
                queue.append((nx, ny))
    return True

result = 0
for i in range(n):
    for j in range(m):
        # if dfs(i, j) == True:
        if bfs(i, j) == True:
            result += 1
print(result)

# Escape Maze
from collections import deque
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))
def bfs_maze():
    queue = deque()
    queue.append((0, 0))
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                data[nx][ny] = data[cx][cy] + 1
                queue.append((nx, ny))
bfs_maze()
print(data[n-1][m-1])
