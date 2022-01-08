# 요세푸스 문제 0

'''
1 ~ N까지의 수들 중에서 K번째 원소를 제거하였을때
제거되는 순서를 출력하시오.
'''

# 풀이1
# N까지 수를 만들고
# K번만큼 반복하면서 k-1번까지는 수는 다른리스트에 저장하고 k번째 수는 결과값에 저장
# 기존 리스트에 앞에서 저장한 리스트를 붙이고 다시 반복

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
circularQueue = deque(list(range(1, N+1)))
result = []

while len(circularQueue) > 1:
    tempQueue = deque([])
    for i in range(K):
        if len(circularQueue) < K:
            if K % 2 == 0:
                pass
        if i == K-1:
            result.append(circularQueue.popleft())
        else:
            tempQueue.append(circularQueue.popleft())

    circularQueue += tempQueue
    print(circularQueue)


print(circularQueue)
print(result)