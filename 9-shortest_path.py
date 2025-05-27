# Dijkstra [valid when all weights are positive]
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b,c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i] : 
            min_value = distance[i] 
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else :
        print(distance[i])



## Improved Dijkstra with headp
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist : 
            continue
        for j in graph[now] :
            cost = dist + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else :
        print(distance[i])



# Floyd-Warshall Algorithm
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else :
            print(graph[a][b], end = ' ')
    print()
    


# Future City
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j :
            graph[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

def future_city():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    distance = graph[1][k] + graph[k][x]

    if distance >= INF:
        print(-1)
    else :
        print(distance)
future_city()



# Telegram
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = [INF] * (n+1)

def telegram(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

    count = 0
    dist = 0
    for i in range(1, n+1):
        if 0 < distance[i] < INF :
            count += 1
            dist = max(dist, distance[i])
    print(count, dist)

telegram(start)