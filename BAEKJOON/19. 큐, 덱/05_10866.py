import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    comment = list(input().split())
    if comment[0] == 'push_front':
        stack = stack[::-1]
        stack.append(comment[1])
        stack = stack[::-1]
    elif comment[0] == 'push_back':
        stack.append(int(comment[1]))
    elif comment[0] == 'pop_front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
            stack = stack[1:]
    elif comment[0] == 'pop_back':
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
    elif comment[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif comment[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])

#29200 80