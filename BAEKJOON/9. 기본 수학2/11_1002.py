# 터렛

'''
(x1, y1), (xn, yn) 사이의 거리 r1
(x2, y2), (xn, yn) 사이의 거리 r2 일때
(xn, yn)의 좌표 개수를 출력하시오.
'''

# 풀이1 (두 원의 접점의 개수)
# 두 점 사이의 거리 sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
# 외접일때
# 1. 두 점 사이의 거리가  < r1 + r2 면 2개
# 2. 두 점 사이의 거리가  > r1 + r2 면 0개
# 3. 두 점 사이의 거리가 == r1 + r2 면 1개
# 내접일때
# 1. 두 점 사이의 거리가 + r2가 > r1 면 2개
# 2. 두 점 사이의 거리가 + r2가 < r1 면 0개
# 3. 두 점 사이의 거리가 + r2가 == r1 면 1개 
# 
# 두 점 사이의 거리가 0이고 r1 == r2 일때 
'''
import math
import sys
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = int(math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
    #두 점 사이의 거리가 0일때
    if distance == 0:
        if r1 == r2:
            print(-1)
        elif r1 > r2 or r1 < r2:
            print(0)
    else:
        # 외접일때
        if distance < r1 + r2:
            print(2)
        elif distance > r1 + r2:
            print(0)
        elif distance == r1 + r2:
            print(1)
        #내접일때
        elif distance + r1 > r2 or distance + r2 > r1:
            print(2)
        elif distance + r1 < r2 or distance + r2 < r1:
            print(0)
        elif distance + r1 == r2 or distance + r2 == r1:
            print(1)
'''
# 왜 틀렸을까...

import sys
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    #두 점 사이의 거리가 0일때
    if distance == 0 and r1 == r2:  # 무한대
        print(-1)
    # 한 점이 같을때
    elif distance == r1 + r2 or distance == abs(r1 - r2):   # 외접 or 내접
        print(1)
    # 외접 일때
    elif abs(r1 - r2) < distance < r1 + r2:     # 두 점에 걸칠때
        print(2)
    # 그 외
    else:
        print(0)

# 29200KB 64ms