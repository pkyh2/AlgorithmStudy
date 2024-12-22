'''
R은 수의 순서를 뒤집는 함수
D는 첫 번째 수를 버리는 함수
'''

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcs = input()
    n = int(input())
    # array1 = input().replace(',', '').rstrip()[1:-1]       DDD [1,2,3,4]
    array1 = input().rstrip()[1:-1].split(',')
    array = deque(array1)
    
    rev = 0     # 뒤집는 횟수
    flag = 1

    # 0처리
    if n == 0:
        array = []
        

    for func in funcs:
        if func == 'R':
            rev += 1
        elif func == 'D':
            if len(array) == 0:
                print('error')
                flag = 0
                break
            else:
                if rev % 2 == 0:
                    array.popleft()
                else:
                    array.pop()

    if flag == 1:
        if rev % 2 == 1:
            array.reverse()
        print('[' + ','.join(array) + ']')