# 회전하는 큐

'''
큐의 크기 N, 뽑아내려는 수의 개수 M
'''

# 풀이1
# 뽑는 수를 순서대로 뽑으면서
# 큐의 맨앞의 숫자와 똑같으면 제거하고
# 그렇지 않으면 뒤로 보낸다.
# 뽑는 수가 전체 큐 길이의 절반 이상에 위치하면 앞으로 보낸다.
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
position = deque(list(map(int, input().split())))  # 2 9 5

dq = deque(list(range(1, N+1)))  # 1 2 3 4 5 6 7 8 9 10
cnt = 0
for i in position:
    while True:
        if i == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(i) > len(dq)//2:
                dq.rotate(1)
                cnt += 1
            else:
                dq.rotate(-1)
                cnt += 1

print(cnt)
# 32368 92