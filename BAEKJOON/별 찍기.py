# 별 찍기 - 2
# N = int(input())
# i = 1
# while N:
#     print(' '* (N-1), end='')
#     print('*'* i)
#     N -= 1
#     i += 1

# n = 5
# arr = [[' '] * n for _ in range(n)]

# for i in range(0, n):
#     for j in range(n-1, n-i-2, -1): # 4, 2
#         print('a[{}][{}]'.format(i, j))
#         arr[i][j] = '*'

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end='')
#     print()

# numbers = [1,2,3]
# print(*(x for x in numbers))
# numbers = [1,2,3]
# print(*numbers)

# 별찍기 
# 별 찍기 - 3
# N = int(input())
# while N > 0:
#     print('*'*N)
#     N -= 1

n = int(input())
arr = [[' '] * n for _ in range(n)]

for i in range(n):
    for j in range(n-i):
        arr[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()

# 별 찍기 - 4
# N = int(input())
# i = 0
# while N > 0:
#     print(' '*i, end='')
#     print('*'*N)
#     i += 1
#     N -= 1

# 별 찍기 - 5
# N = int(input())
# i = 1
# while N > 0:
#     print(' ' * (N-1), end='')
#     print('*' * (i-1), end='')
#     print('*' * i)
#     i += 1
#     N -= 1

# 별 찍기 - 6
# N = int(input())
# i = 0
# while N > 0:
#     print(' ' * i, end='')
#     print('*' * (N), end='')
#     print('*' * (N-1))
#     i += 1
#     N -= 1

# 별 찍기 - 7
# N = int(input())

# i = 1
# j = N
# while j > 0:
#     print(' ' * (j-1), end='')
#     print('*' * (i-1), end='')
#     print('*' * i)
#     i += 1
#     j -= 1
# i = 1
# j = N - 1
# while j > 0:
#     print(' ' * i, end='')
#     print('*' * (j), end='')
#     print('*' * (j-1))
#     i += 1
#     j -= 1

# 별 찍기 - 8
# N = int(input())
# i = N
# star = 1
# while i > 0:
#     print('*' * star, end='')
#     print(' ' * (i-1), end='')
#     print(' ' * (i-1), end='')
#     print('*' * star, end='')
#     print()
#     star += 1
#     i -= 1

# i = 2
# star = N-1
# while star > 0:
#     print('*' * star, end='')
#     print(' ' * (i-1), end='')
#     print(' ' * (i-1), end='')
#     print('*' * star, end='')
#     print()
#     star -= 1
#     i += 1 