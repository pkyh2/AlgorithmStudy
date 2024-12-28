# a = float(input())
# print(format(a, ".2f"))

#f1, f2 = map(float, input().split())
#print(format(f1/f2, '.3f'))

# a, b = map(int, input().split())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(format(a / b, '.2f'))


# a, b, c = map(int, input().split())

# print('{} {:.2f}'.format(a+b+c, (a+b+c)/3))

# a, b = map(int, input().split())
# if a != b:
#     print(True)
# else:
#     print(False)

# n = int(input())
# print(bool(n))

# a, b = map(int, input().split())
# c = bool(a)
# d = bool(b)
# print(not c and not d)

# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print('A')
#     else:
#         print("B")
# else:
#     if a % 2 == 0:
#         print('C')
#     else:
#         print("D")

# a = int(input())
# if a >= 90:
#     print('A')
# elif a >=70:
#     print('B')
# elif a >= 40:
#     print('C')
# else:
#     print('D')

# word = input()
# if word == 'A':
#     print('best!!!')
# elif word == 'B':
#     print('good!!')
# elif word == 'C':
#     print('run!')
# elif word == 'D':
#     print('slowly~')
# else:
#     print('what?')

# a = int(input())
# if a == 12 or a == 1 or a == 2:
#     print('winter')
# elif a == 3 or a == 4 or a == 5:
#     print('spring')
# elif a == 6 or a == 7 or a == 8:
#     print('summer')
# elif a == 9 or a == 10 or a == 11:
#     print('fall')

# n = 1
# while n != 0:
#     n = int(input())
#     if n != 0:
#         print(n)

# a = int(input())
# while a > 0:
#     a -= 1
#     print(a)

# alpha = ord(input())
# t = ord('a')                # 97
# while t <= alpha:
#     print(chr(t), end=' ')
#     t += 1

# a = int(input())
# sum = 0
# for i in range(1, a+1):
#     if i % 2 == 0:
#         sum += i

# print(sum)
# list1 = []
# while True:
#     alpha = input()
#     if alpha != 'q':
#         print(alpha)

# a = int(input())
# sum = 0
# i = 0
# while sum < a:
#     i += 1
#     sum += i

# print(i)

# n, m = map(int, input().split())
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# a = int(input(), 16)        # 16진수로 정수 값 받기

# for i in range(1, 16):
#     print('{:X}*{:X}={:X}'.format(a, i, a*i))

# a = int(input())
# for i in range(1, a+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("X", end=' ')
#     else:
#         print(i, end=' ')


# r, g, b = map(int, input().split())
# cnt = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
#             cnt += 1

# print(cnt)

'''
1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.

'''
# h, b, c, s = map(int, input().split())
# cdSound = h * b * c * s
# pcm = cdSound / 8 / 1024 / 1024
# print(format(pcm, '.1f'), 'MB')

# w, h, b = map(int, input().split())
# bmp = w * h * b
# result = bmp / 8 / 1024 / 1024

# print('{:.2f}'.format(result), 'MB')

# a = int(input())
# i = 1
# sum = 0
# while True:
#     sum += i
#     i += 1
#     if sum >= a:
#         break

# print(sum)

# a = int(input())
# for i in range(1, a+1):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i, end=' ')

# a, b, n = map(int, input().split())

# cnt = 1
# sum = a
# while True:
#     if cnt == n:
#         print(sum)
#         break
#     sum *= b
#     cnt += 1

'''
a초기값, m곱할값, d더할값 n몇번째
'''
# a, m, d, n = map(int, input().split())

# cnt = 1
# sum = a
# while True:
#     if cnt == n:
#         print(sum)
#         break
#     sum *= m
#     sum += d
#     cnt += 1

# a, b, c = map(int, input().split())
# d = 1
# while d % a != 0 or d % b != 0 or d % c != 0:
#     d += 1
# print(d)

# n = int(input())
# a = list(map(int, input().split()))

# d = [0 for _ in range(24)]

# for i in range(n):
#     d[a[i]] += 1

# for i in range(1, len(d)):
#     print(d[i], end=' ')


# n = int(input())
# a = list(map(int, input().split()))
# for i in range(n-1, -1, -1):
#     print(a[i], end=' ')

# n = int(input())
# a = list(map(int, input().split()))
# print(min(a))

# d = [[0 for _ in range(20)] for _ in range(20)]

# n = int(input())        # 몇번 찍을건지 좌표를

# for _ in range(n):
#     x, y = input().split()
#     d[int(x)][int(y)] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=' ')
#     print()

# 6096
# d = [[int(x) for x in input().split()] for _ in range(19)]
# print(d[9][9])
# n = int(input())
# for _ in range(n):
#     x, y = input().split()          # 10 10
#     for j in range(0, 19):          # 0 ~ 19
#         if d[j][int(y)-1] == 1:
#             print(d[j][int(y)-1])
#             if d[j][int(y)-1] == d[int(x)-1][j]:
#                 continue
        
#             d[j][int(y)-1] = 0

#         if d[int(x)-1][j] == 1:
#             if d[int(x)-1][j] == d[j][int(y)-1]:
#                 continue
#             else:
#                 d[int(x)-1][j] = 0

# for i in range(0, 19):
#     for j in range(0, 19):
#         print(d[i][j], end=' ')
#     print()

d = [[int(x) for x in input().split()] for _ in range(19)]
n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(19):
        if d[j][int(y)-1] == 1:    #d[9][9]
            d[j][int(y)-1] = 0
        elif d[j][int(y)-1] == 0:
            d[j][int(y)-1] = 1

        if d[int(x)-1][j] == 1:
            d[int(x)-1][j] = 0
        elif d[int(x)-1][j] == 0:
            d[int(x)-1][j] = 1

for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=' ')
    print()

#6097
# h, w = map(int, input().split())    # 가로 세로
# board = [[0 for _ in range(w)] for _ in range(h)]   # board 생성
# n = int(input())                    # 막대의 개수
# for _ in range(n):
#     l, d, x, y = map(int, input().split())  # 길이, 방향 0가로, 1세로, 좌표
#     if d == 0:
#         for i in range(l):
#             board[x-1][y-1] = 1
#             y += 1
#     elif d == 1:
#         for i in range(l):
#             board[x-1][y-1] = 1
#             x += 1

# for i in range(h):
#     for j in range(w):
#         print(board[i][j], end=' ')
#     print()

# #6098
# board = [[int(x) for x in input().split()] for _ in range(10)]

# i = 1
# j = 1
# while True:

#     if board[i][j] == 0:
#         board[i][j] = 9
#         j += 1
#     elif board[i][j] == 1:
#         j -= 1
#         i += 1
#         if board[i][j] == 1:
#             break
#     elif board[i][j] == 2:
#         board[i][j] = 9
#         break
    
# for i in range(10):
#     for j in range(10):
#         print(board[i][j], end=' ')
#     print()