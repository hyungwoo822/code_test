### 23. Language, English, Mathematcis
n = int(input())
data = []
for i in range(n):
    data.append(input().split())

data.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in data:
    print(student[0])


### 24. Antenna
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
dist = 1e9
result = None
for i in range(len(houses)):
    pos = houses[i]
    temp = 0
    for house in houses:
        temp += abs(houses[i] - house)
    if dist > temp : 
        dist = temp
        result = pos
print(result)



### 25. Failure Rate
def solution(N, stages):
    answer = []
    failure = []
    for i in range(1, N+1):
        leng = 0
        fail = 0
        for stage in stages:
            if stage >= i:
                leng += 1
                if i == stage :
                    fail += 1
        if leng == 0:
            failure.append((i, 0))
        else :
            failure.append((i, fail / leng))
    failure.sort(key = lambda x : x[1], reverse=True)
    answer = [i[0] for i in failure]
    return answer
N = int(input())
stages = list(map(int, input().split()))
print(solution(N, stages))

### 25.1. Failure Rate2
def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        fail = stages.count(i)
        if total == 0:
            answer.append((i, 0))
        else :
            answer.append((i, fail / length))
        length -= fail
    answer.sort(key = lambda x : x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer


### 26. Ordering Cards
n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))
cards.sort()
result = 0
leng = len(cards)
for i in range(leng):
    if i == 0:
        result += (leng - 1) * cards[i]
    else :
        result += (leng - 1) * cards[i]
        leng -= 1
print(result)

### 26.1 Ordering cards : queue
import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
result = 0

while len(heap) != 1 :
    one = heapq.heappop(heap)
    two = heapq.heapopp(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)