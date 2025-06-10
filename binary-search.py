# ### 27. Count specific number in the orderd array
# n, x = map(int, input().split())
# data = list(map(int, input().split()))

# def count_by_value(array, x):
#     n = len(array)

#     a = first(array, x, 0, n-1)

#     if a == None:
#         return 0
#     b = last(array, x, 0, n-1)

#     return b-a+1
    
# def first(array, target, start, end):
#     if start > end :
#         return None
#     mid = (start + end) // 2
#     if (mid == 0 or target > array[mid-1]) and array[mid] == target:
#         return mid
#     elif array[mid] >= target:
#         return first(array, target, start, mid -1)
#     else:
#         return first(array, target, mid+1, end)
    
# def last(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) //2
#     if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
#         return mid
#     elif target >= array[mid] :
#         return last(array, target, mid + 1, end)
#     else:
#         return last(array, target, start, mid -1)

            
# count = count_by_value(data, x)
# if count == 0:
#     print(-1)
# else :
#     print(count)


# ### 27.2 Count specific number in the orderd array
# from bisect import bisect_right, bisect_left
# n, x = map(int, input().split())
# data = list(map(int, input().split()))

# left = bisect_left(data)
# right = bisect_right(data)
# count = right - left

# if count == 0:
#     print(-1)
# else:
#     print(count)



# ### 28. Find fix point
# n = int(input())
# data = list(map(int, input().split()))

# def fix_point(n, data):
#     start = 0
#     end = n-1
#     while start <= end :
#         mid = (start+end) // 2
#         if data[mid] == mid:
#             return mid
#         elif data[mid] < mid:
#             start = mid + 1
#         else:
#             end = mid -1
#     return -1
# print(fix_point(n, data))
                
        

### 29. Install wifi
n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
    

    