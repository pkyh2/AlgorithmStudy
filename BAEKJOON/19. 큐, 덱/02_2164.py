# 카드 2

'''
맨앞에 카드를 한장 버린다.
그 다음 카드를 덱 맨뒤로 옮긴다.
카드가 한장 남으면 출력하고 종료한다. 
'''
# 풀이1(반복문)
# 생성된 리스트에서
# 리스트의 길이가 1이 될때까지 동작을 반복
# 첫번째 원소를 지우고, 두번째 원소를 변수에 담고 지운다음
# 두번째 원소를 마지막 원소 뒤에 추가해준다.
# import sys
# input = sys.stdin.readline

# queue = list(range(1, int(input())+1))
# while len(queue) != 1:
#     del queue[0]
#     temp = queue[0]
#     del queue[0]
#     queue.append(temp)

# print(*queue)
# 시간초과

# 풀이2 (클래스 이용)
# import sys
# input = sys.stdin.readline

# # 큐 클래스 정의
class Queue():
    def __init__(self):     # 큐 생성
        self.data = []

    def enQueue(self, e):   # 0번째 원소에 큐삽입
        self.data.insert(0, e)

    def deQueue(self):
        if self.is_empty(): # 큐가 비어있다면
            raise IndexError("Queue is empty")
        else:
            return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.data[-1]

    def is_empty(self):     # 큐가 비어있으면 True를 return
        return len(self.data) == 0

    def size(self):
        return len(self.data)

N = int(input())
Q = Queue() # 큐 객체 생성
for i in range(1, N+1):
    Q.enQueue(i)

while Q.size() > 1:
    Q.deQueue()
    Q.enQueue(Q.deQueue())

print(Q.data[0])
# 시간초과

# 풀이3(queue라이브러리 이용)
import sys
from collections import deque

input = sys.stdin.readline

queue = deque(list(range(1, int(input())+1)))   # [1, 2, 3, 4, 5, 6]
while(len(queue) > 1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])