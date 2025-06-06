# code_test
---

# 🏆 코딩테스트 실전 파이썬 내장 함수 & 라이브러리 총정리

---

## 1. **정렬**

* `sorted(iterable, key=None, reverse=False)`

  * 리스트, 튜플 등 반복 가능한 객체 정렬해서 **새 리스트 반환**
  * key: 정렬 기준 함수 (ex: key=lambda x: x\[1])
  * reverse: True면 내림차순

* `list.sort(key=None, reverse=False)`

  * 리스트 자체를 정렬 (**in-place**)
  * 반환값 없음

```python
a = [3, 1, 4, 2]
b = sorted(a)         # [1, 2, 3, 4]
a.sort()              # a가 [1, 2, 3, 4]로 바뀜
```

---

## 2. **우선순위 큐 (힙)**

* **최소 힙**: `heapq` 모듈
  → 항상 가장 작은 값이 먼저 나옴

```python
import heapq

arr = [5, 3, 7, 1]
heapq.heapify(arr)       # 리스트를 최소 힙으로 변환
heapq.heappush(arr, 2)   # 2 삽입
min_val = heapq.heappop(arr)  # 1 반환
```

* **최대 힙**:
  모든 값을 -붙여서 최소 힙처럼 사용

```python
import heapq

arr = [5, 3, 7, 1]
max_heap = [-x for x in arr]
heapq.heapify(max_heap)
max_val = -heapq.heappop(max_heap)
```

---

## 3. **카운팅**

* **빈도수 세기**: `collections.Counter`

```python
from collections import Counter

s = 'abcaab'
count = Counter(s)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

---

## 4. **deque (양방향 큐)**

* 양쪽에서 삽입/삭제가 매우 빠름
  (스택+큐를 섞은 느낌, BFS 구현할 때 자주 사용)

```python
from collections import deque

dq = deque([1,2,3])
dq.append(4)      # 뒤에 삽입
dq.appendleft(0)  # 앞에 삽입
dq.pop()          # 뒤에서 제거
dq.popleft()      # 앞에서 제거
```

---

## 5. **기본 자료구조 변환**

* 리스트 ↔ 집합(set) ↔ 딕셔너리(dict) 변환, 중복 제거

  ```python
  a = [1,2,2,3,3,3]
  set_a = set(a)  # {1,2,3}
  list_a = list(set_a)  # [1,2,3]
  ```

---

## 6. **조합/순열**

* 순열: `itertools.permutations`
* 조합: `itertools.combinations`

```python
from itertools import permutations, combinations

a = [1,2,3]
print(list(permutations(a, 2)))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
print(list(combinations(a, 2)))  # [(1,2), (1,3), (2,3)]
```

---

## 7. **최대공약수, 최소공배수**

```python
import math

gcd = math.gcd(12, 18)  # 6
lcm = 12 * 18 // math.gcd(12, 18)  # 36
```

---

## 8. **입출력**

* 빠른 입력:

  ```python
  import sys
  input = sys.stdin.readline
  ```
* 여러 줄 입력 받아야 할 때 매우 유용

---

## 9. **기타 유용한 함수들**

* `enumerate()`: 인덱스랑 값 동시에
* `zip()`: 여러 리스트 묶기
* `map()`: 리스트/입력값 한 번에 함수 적용
* `sum()`: 리스트 전체 합
* `min()`, `max()`: 최소/최대값
* `any()`, `all()`: 조건에 하나라도/모두 True

---

## 10. **정렬 기준이 복잡할 때**

* `lambda` 사용

  ```python
  a = [(1, 'b'), (3, 'a'), (2, 'c')]
  a.sort(key=lambda x: x[1])  # 문자열 기준 정렬
  ```

---


# 11. **any() / all()**

* 리스트(혹은 반복 가능한 객체)에서
  **하나라도 True**면 `any()`가 True
  **전부 True**여야 `all()`이 True

### 사용 예시

```python
arr = [0, 0, 3, 0]

print(any(arr))  # True (3이 있으니까 True)
print(all(arr))  # False (0이 있어서 모두 True가 아님)

arr2 = [1, 2, 3, 4]
print(all(x > 0 for x in arr2))    # True (모두 양수)
print(any(x % 2 == 0 for x in arr2))  # True (짝수 하나라도 있으면 True)
```

### 실전 활용

* "리스트에 0이 하나라도 있으면 실패 처리"
* "모든 점수가 60점 이상이어야 합격"

---

# 12. **zip()**

* **여러 리스트를 같은 인덱스끼리 묶어서 튜플로 반환**

### 사용 예시

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

for x, y in zip(a, b):
    print(x, y)
# 출력:
# 1 a
# 2 b
# 3 c

# 리스트로 변환
zipped = list(zip(a, b))
print(zipped)   # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 실전 활용

* 두 개 이상의 리스트를 같이 순회할 때
* 예를 들어 (학생, 점수) 쌍 만들기, 좌표 쌍 만들기 등

---

# 13. **map()**

* **리스트나 입력값 전체에 함수를 한 번에 적용**

### 사용 예시

```python
a = ['1', '2', '3']
nums = list(map(int, a))   # ['1', '2', '3'] → [1, 2, 3]

# 제곱으로 변환
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))  # [1, 4, 9, 16]
```

* `map(함수, 반복가능객체)`

### 실전 활용

* 입력받은 문자열 숫자를 한 번에 int로 변환
  `a = list(map(int, input().split()))`
* 배열 전체에 어떤 연산 적용할 때

---


### 실전 활용

* 정렬 기준이 복잡할 때 (key에)
* map과 함께 즉석에서 함수 적용할 때

---

# 💡 **실전 한 번에 써보기**

```python
scores = [70, 85, 90, 55]

# 모든 점수가 60점 이상이어야 합격
print(all(map(lambda x: x >= 60, scores)))  # False

# 짝수 있는지 확인
print(any(map(lambda x: x % 2 == 0, scores)))  # True

# 이름, 점수 리스트에서 점수로 정렬
names = ['철수', '영희', '민수']
scores = [70, 85, 90]
for name, score in sorted(zip(names, scores), key=lambda x: x[1], reverse=True):
    print(name, score)
# 민수 90
# 영희 85
# 철수 70
```

---


# ✅ **실전 팁**

1. **내장 함수/모듈 적극 활용**
   (직접 구현 요구 없으면 무조건 씀)
2. **Counter, heapq, deque, itertools 등 10초 안에 쓸 줄 알면 문제 풀이 속도가 확 오른다**
3. **정렬, 우선순위큐, 조합/순열 등은 90% 이상 문제에서 한 번쯤 꼭 등장**

