array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# selection sort 

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort(array))

# insertion sort
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
            else :
                break
    return array

print(insertion_sort(array))


# Quick Sort

# recursively call function
def quick_sort(array, start, end):
    if start >= end :
        return
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left+=1
        while right > start and array[right] >= array[pivot]:
            right-=1
        if left > right :
            array[pivot], array[right] = array[right], array[pivot]
        else : 
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)

# recursively call function [using python advanced grammar]
def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)
print(quick_sort2(array))



# Merge Sort
def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h] :
            merged_arr.append(low_arr[l])
            l += 1
        else :
            merged_arr.append(high_arr[h])
            h += 1
    # merge rest array elements
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr


# Heap Sort
def heapify(unsorted, index, heap_size):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  
  if left < heap_size and unsorted[right] > unsorted[largest]:
    largest = left
    
  if right < heap_size and unsorted[right] > unsorted[largest]:
    largest = right
    
  if largest != index:
    unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
    heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
  n = len(unsorted)
  
  for i in range(n // 2 - 1, -1, -1):
    heapify(unsorted, i, n)
    
  for i in range(n - 1, 0, -1):
    unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
    heapify(unsorted, 0, i)

  return unsorted




# Count Sort
def count_sort(array):
    count = [0] * (max(array) + 1)
    for i, data in enumerate(array):
        count[data] += 1
    for i, data in enumerate(count) :
        for j in range(data):
            print(i, end=' ')

print(count_sort(array))


# top-to-bottom
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
print(array[::-1])
array = sorted(array, reverse=True)
print(array)

# lowest scored student 
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], input_data[1]))
array = sorted(array, key=lambda student:student[1])
for i in array:
    print(i[0], end=' ')

# convert elements of two array
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
    if a[i] < b[-i]:
        a[i], b[-i] = b[-i], a[i]
    else :
        break
print(sum(a))
    

