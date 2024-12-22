# 좌표 정렬하기
'''
import sys

N = int(sys.stdin.readline())

point = []
for i in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    point.append(xy)

for i in range(1, len(point)):
    for j in range(i, 0, -1):
        if point[j - 1][0] > point[j][0]:
            point[j - 1][0], point[j][0] = point[j][0], point[j - 1][0]
            point[j - 1][1], point[j][1] = point[j][1], point[j - 1][1]
        elif point[j - 1][0] == point[j][0]:
            if point[j - 1][1] > point[j][1]:
                point[j - 1][1], point[j][1] = point[j][1], point[j - 1][1]
        else:
            break

for i in point:
    for j in i:
        print(j, end=' ')
    print()
'''
# 시간초과...
# 합병정렬 써야되나보다

# 풀이2
# sorted(key=) 를 이용한 해결법

import sys
input = sys.stdin.readline

N = int(input())
point = []
for i in range(N):
    xy = list(map(int, input().split()))
    point.append(xy)

point = sorted(point, key=lambda x: (x[0], x[1]))   # x[0] 기준으로 정렬인데 묶어서
for i in point:
    for j in i:
        print(j, end=' ')
    print()
    
# 57672 468