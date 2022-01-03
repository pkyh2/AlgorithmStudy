# 제로

'''
stack에 자료를 입력받는데 0을 입력받으면 pop연산을 한다.
stack의 합을 출력하시오.
'''

import sys
input = sys.stdin.readline

T = int(input())

stack = []
for _ in range(T):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
# 29980 108