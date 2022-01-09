# 회전하는 큐

'''
큐의 크기 N, 뽑아내려는 수의 개수 M
'''

# 풀이1
# 1 ~ N까지 덱을 만든다.
# 찾으려고 하는 인덱스가 N의 절반이상이면
# 뒤에서부터 값을 앞으로 옮기면서 cnt를 증가시킨다.
# 그렇지 않으면 앞에서 뒤로 옮기면서 cnt를 증가시킨다.
# 원하는 숫자를 찾으면 제거한다.
# 원하는 숫자의 인덱스를 찾는다 그게 절반 이상이면 뒤에서 찾고 아니면 밑에서 찾는다.

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
position = list(map(int, input().split()))  # 2 9 5

deque = deque(list(range(1, N+1)))  # 1 2 3 4 5 6 7 8 9 10
cnt = 0
while len(position):
    i = 0
    if position[i] == deque[i]:
        if i <= len(deque) // 2:
            deque.popleft()
        else:
            deque.pop()