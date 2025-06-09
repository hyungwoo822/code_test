# ### 07. Lucky Straight
# s = input()
# leng = len(s)
# result1, result2 = 0, 0
# for i in range(leng // 2):
#     result1 += int(s[i])
#     result2 += int(s[-i-1])
# if result1 == result2:
#     print("LUCKY")
# else:
#     print("READY")


# ### 08. Reorder string
# import re
# s = input()
# alpha = []
# number = []
# for i in s:
#     if i.isalpha():
#         alpha.append(i)
#     else:
#         number.append(i)
#     alpha.sort()
# temp = 0
# for i in number:
#     temp += int(i)
# alpha.append(temp)
# for i in alpha:
#     print(i, end = '')


# ### checked
# ### 09. Compress string
# s = input()
# answer = len(s)
# for step in range(1, len(s) // 2 + 1):
#     compressed = ""
#     prev = s[0:step]
#     count = 1
#     for j in range(step, len(s), step):
#         if prev == s[j:j+step]:
#             count += 1
#     else :
#         compressed += str(count) + prev if count >= 2 else prev
#         prev = s[j:j+step]
#         count = 1
#     compressed += str(count) + prev if count >= 2 else prev
#     answer = min(answer, len(compressed))
# print(answer)



# ### 10. lock and key
# def turn_clockwise(array):
#     n = len(array)
#     m = len(array)
#     result = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = array[i][j]
#     return result

# def check(new_lock):
#     lock_leng = len(new_lock) // 3
#     for i in range(lock_leng, lock_leng * 2):
#         for j in range(lock_leng, lock_leng * 2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0] * (n * 3) for _ in range(n * 3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i][j] = lock[i][j]
    
#     for rotation in range(4):
#         key = turn_clockwise(key)
#         for x in range(n*2) :
#             for y in range(n*2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]x
#                 if check(new_lock) == True:
#                     return True
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
#     return False


### 11. Snake



