import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    comment = list(input().split())
    if comment[0] == 'push':
        stack.append(int(comment[1]))
    elif comment[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comment[0] == 'size':
        print(len(stack))
    elif comment[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif comment[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])
# 29200 76