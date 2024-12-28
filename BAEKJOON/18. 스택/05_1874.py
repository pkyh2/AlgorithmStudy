'''
1부터 n까지에 수에 대해 차례로 
[push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop]
연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

그니까 n을 입력했을 때 1 ~ n까지의 숫자들을
스택 연산을 통해 아래 입력값 순서로 출력할 수 있는지
'''

# 풀이1
# import sys
# input = sys.stdin.readline

# n = int(input())
# numbers = list(range(1, n+1))

# result = []
# for _ in range(n):
#     result.append(int(input()))

# stack = []
# outside = []

# for i in result:
#     for j in numbers:
#         if i not in stack:
#             stack.append(j)
#             numbers.remove(j)
#             print('+')
#         elif i in stack:
#             stack.pop()
#             print('-') 

# print(stack)


# 풀이2
# import sys
# input = sys.stdin.readline

# n = int(input())
# numbers = list(range(1, n+1))

# result = []
# for _ in range(n):
#     result.append(int(input()))

# stack = []

# for i in result:
#     for j in range(len(numbers)):
#         if i >= numbers[j]:
                
#             if numbers[j] not in stack:
#                 stack.append(numbers[j])
#                 print('+')
#                 # result에 최댓값일 때는 i보다 큰 경우가 없기 때문에 else문으로 가지 않는다.
#                 if i == max(result):
#                     stack.pop()
#                     numbers.remove(i)
#                     print('-')
#         else:
#             stack.pop()
#             numbers.remove(i)
#             print('-')
#             break

# if len(stack) > 0:
#     print('NO')


# 풀이3
import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
cnt, pointer= 1, 0
for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        pointer = 1
        break

if pointer == 0:
    for i in result:
        print(i)
        
# 31296 220