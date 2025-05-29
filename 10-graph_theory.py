# Find disjoint set [Union]
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
print(parent)
for i in range(1, v+1):
    print(find_parent(parent ,i), end = ' ')
print()
print('parent table : ', end = ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')




# Path compression disjoint set
# Find disjoint set [Union]
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
print(parent)
for i in range(1, v+1):
    print(find_parent(parent ,i), end = ' ')
print()
print('parent table : ', end = ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')



# Find cycle
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) :
        cycle = True
        break
    else :
        union_parent(parent, a, b)
if cycle:
    print('cycle')
else:
    print('not cycle')



# Kruskal Algorithm
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)



# Topology Sorting
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(v):
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        v = q.popleft()
        result.append(v)
        for i in graph[v]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end = ' ')
topology_sort(v)



# Team forming
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for i in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union_parent(parent, a, b)
    else :
        if find_parent(parent, a) != find_parent(parent, b):
            print("NO")
        else:
            print("YES")


# City Division Plan
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n, m = map(int, input().split())
edges = []
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
edges = sorted(edges, key = lambda x:x[2])
result = 0
last = 0
for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = max(last, cost)
result -= last
print(result)



# Curriculum
from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1, v+1):
        print(result[i])

topology_sort()