### 01. Adventure Guild
n = int(input())
man = list(map(int, input().split()))
result = 0
man.sort()
grp_temp = 0
for i in man:
    grp_temp += 1
    if i <= grp_temp:
        grp_temp = 0
        result += 1
print(result)


### 02. Multiply or Addition
s = input()
result = 0
for i in s:
    temp1 = result + int(i)
    temp2 = result * int(i)
    if temp1 > temp2:
        result = temp1
    else:
        result = temp2
print(result)



### 03. Reversed String
s = input()
result = 0
cond = 0
temp = s[0]
for i in s[1:]:
    if i == temp:
        continue
    elif i != temp:
        temp = i
        cond += 1
        if cond % 2 == 0:
            result += 1
print(result)


### checked
### 04. Amount cannot be made 
n = int(input())
wallet = list(map(int, input().split()))
wallet.sort()
target = 1
for coin in wallet:
    if target < coin:
        break
    target += coin
print(target)


### 05. Picking bowling ball
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = 0
for ball1 in data:
    for ball2 in data[ball1:]:
        if ball1 >= ball2 :
            continue
        else:
            print(f"(n, m) = ({ball1}, {ball2})")
            result +=1
print(result)


### checked
### 06. Muzi's Mukbang Live
# my correct answer
import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    length = len(food_times)
    previous = 0
    sum_value = 0
    while q:
        now = q[0][0]
        spend = (now-previous) * length
        if sum_value + spend > k :
            break
        heapq.heappop(q)
        sum_value += spend
        length -= 1
        previous = now
    
    result = sorted(q, key=lambda x:x[1]) 
    return result[(k-sum_value) % length][1]
    
# correct answer
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0
    previous= 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -=1
        previous = now
    
    result = sorted(q, key=lambda x:x[1])
    return result[(k-sum_value) % length][1]



# # incorrect answer
# food_times = list(map(int, input().split()))
# k = int(input())
# size = len(food_times)
# idx = 0
# for i in range(k):
#     while food_times[idx] == 0:
#         idx += 1
#         if idx >= size:
#             idx = 0
        
#     food_times[idx] -= 1
#     idx += 1
#     if idx >= size:
#         idx = 0

# for i, food in enumerate(food_times):
#     if food == 0:
#         continue
#     else:
#         print(i+1)




