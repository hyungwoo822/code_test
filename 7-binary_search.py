# # Seqeuntial searching
# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target :
#             return i + 1
# print("생성할 원소 갯수를 입력하고 찾을 문자열을 입력하시오 : ")
# input_data = input().split()
# n = int(input_data[0])
# target = input_data[1]

# print(" 앞서 적은 n 개 만큼 문자열 입력 : ")
# array = input().split()
# print(sequential_search(n, target, array))

# # Binary Search Recusrively
# def binary_search(array, target, start, end):
#     if start > end : 
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target : 
#         return binary_search(array, target, start, mid-1)
#     else :
#         return binary_search(array, target, mid+1, end)
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None : 
#     print(" no elements in array")
# else :
#     print(result + 1)

# # Binary Search iteratively
# def binary_search_iterate(array, target, start, end):
#     while start <= end :
#         mid = (start + end) // 2
#         if array[mid] == target :
#             return mid
#         elif array[mid] < target :
#             start = mid + 1
#         else :
#             end = mid -1
#     return None 

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search_iterate(array, target, 0, n-1)
# if result == None : 
#     print(" no elements in array")
# else :
#     print(result + 1)

# # Searching machinery - count sort
# n = int(input())
# array = [0] * 100001
# for i in map(int, input().split()):
#     array[i] = 1
# m = int(input())
# x = list(map(int, input().split()))

# for i in x :
#     if array[i] == 1:
#         print('yes', end = ' ')
#     else :
#         print('no', end = ' ')

# # Searching Macinery - set
# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))
# for i in x :
#     if i in array:
#         print('yes', end = ' ')
#     else :
#         print('no', end = ' ')

# Making DDEOK
n,m = list(map(int, input().split()))
array = list(map(int, input().split()))
start = 0
end = max(array)
def ddeok_binary_search(array, target, start, end, result = 0):
    if start > end : 
        return result
    mid = (start + end) // 2
    sum = 0
    for i in array : 
        if i - mid > 0 :
            sum += (i - mid)
    if sum < target : 
        return ddeok_binary_search(array, target, start, mid - 1, result)
    else:
        return ddeok_binary_search(array, target, mid + 1, end , mid)
        
print(ddeok_binary_search(array, m, start, end))