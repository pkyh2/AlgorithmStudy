# 프린터 큐

'''
큐 문서의 수와 중요도가 주어졌을 때, 어떤 문서가 몇 번째로 인쇄 되는지 알아내는 것이다.
ex) [A, B, C, D]의 중요도가 2, 1, 4, 3이면 C가 1번째로 출력되고 A가 3번째로 출력된다.
'''

# 풀이1
# 입력 값을 입력받는다.
# 중요도 길이만큼 queue의 0으로 초기화 한다.
# M값을 queue의 index에 넣는다.
# 중요도를 반복하면서 제일 큰수면 제거하고 cnt를 올린다.
# 이때 제거된 수와 M값이 같으면 반복문을 종료한다.
# 결과값으로 cnt를 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, index = map(int, input().split())
    importance = deque(list(map(int, input().split()))) # [1, 2, 3, 4]
    queue = deque([0] * len(importance))                # [0, 0, M, 0]
    queue[index] = M
    cnt = 1

    while len(importance) >= 1:              # [1, 2, 3, 4]
        i = 0
        if importance[i] == max(importance): # [0, 0, M, 0]
            if queue[i] == M:
                print(cnt)
                break
            else:
                cnt += 1
                importance.popleft()
                queue.popleft()
        else:
            importance.rotate(-1)
            queue.rotate(-1)
# 32360 100