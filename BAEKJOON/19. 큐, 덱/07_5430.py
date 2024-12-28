# AC

'''
두 가지 함수 R(뒤집기), D(버리기)
배열이 비어있는데 D를 사용하면 에러 발생
"RDD"는 뒤집고, 다음 처음 두 수를 버린다.
1. T
2. 수행할 함수
3. 배열의 길이
4. 배열
'''

#풀이1
# 입력값이 주어지고 나면, 입력으로 주어진 함수 문자열을 반복한다.
# 주어진 변수에 따라 맞는 함수를 실행한다.

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    functions = input()
    dqLen = int(input())
    list1 = list(input())
    dq = deque()
    numString = ''

    for i in list1:
        if i in '[,]':
            dq.append(numString)
            numString = ''
        else:
            numString += i
    
    dq.remove(dq[0])
    if dq[0] != '':
        dq = deque(list(map(int, dq)))
    else:
        dq.remove(dq[0])

    for i in functions:
        if i == 'R':
            for i in range(len(dq)//2):
                dq[i], dq[len(dq)-i-1] = dq[len(dq)-i-1], dq[i]
        elif i == 'D':
            if len(dq) == 0:
                print('error')
            else:
                dq.popleft()
    if len(dq):
        print(list(dq))
#시간초과

# 풀이2
# 1. len이 0일 때 처리
# 2. R이 홀수면 pop(), 짝수면 popleft()

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    functions = input()
    dqLen = int(input())
    list1 = input().rstrip()[1:-1].split(',')
    dq = deque(list1)

    if dqLen == 0:
        dq = []

    flag = 0
    cnt = 0
    for j in functions:         #[1, 2, 3, 4]
        if j == 'R':            # RRDD
            cnt += 1
        elif j == 'D':
            if len(dq) == 0:
                flag = 1
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    
    if flag == 0:
        if cnt % 2 == 0:
            print('[' + ','.join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ','.join(dq) + ']')
# 44564 240