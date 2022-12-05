##연습문제
#숫자 입력받아서 큰수 만들기

#n개의 수 받기
#m 총 더하는 횟수
#k 가장 큰수 더할 수 있는 수
# print("n, m, k 입력하세요 : ", end='')
# n, m, k = map(int, input().split())
#
# print(n, "개만큼 입력하세요 : ", end='')
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

###############################
# 행에서 가장 작지만 모든 행중에서는 큰 수를 뽑기###############################

# n, m = map(int, input().split())
# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
#
# print(result)

#1 만들기 ###############################

# n, k = map(int, input().split())
# count = 0
# while True:
#     if n == 1:
#         break
#     elif n % k == 0:
#         n /= k
#         count += 1
#     else:
#         n -= 1
#         count += 1
#
# print(count)

# 정사각형에서 이동하는 것 만들기 LRUD ###############################

# n = int(input())
# x, y = 1, 1
# move =input().split()
# move_types = ['L', 'R', 'U', 'D']
# mx = [0,0,-1,1]
# my = [-1,1,0,0]
#
# for m in move:
#     for i in range(len(move_types)):
#         if m == move_types[i]:
#             nx = x + mx[i]
#             ny = y + my[i]
#     if nx < 1 or nx > n or ny < 1 or ny >n:
#         continue
#
#     x, y = nx, ny
# print(x, y)


# 3이 들어간 시간대 더하기 ###############################

# h = int(input())
# count =0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print (count)

# 왕실 나이트 ###############################
#   a  b  c  d  e  f  g  h
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# cur = input()
# row = int(cur[1])
# colum = int(ord(cur[0])) - int(ord('a')) + 1
#
# move_list = [(-2, + 1), (-2, -1), (+2, +1), (+2, -1), (-1, + 2), (-1, -2), (+1, -2), (+1, +2)]
#
# result = 0
# for step in move_list:
#     next_row = row + step[0]
#     next_colum = colum + step[1]
#
#     if next_row >= 1 and next_row <= 8 and next_colum >=1 and next_colum <= 8:
#         result += 1
# print(result)

#






