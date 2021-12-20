# 좌표 정렬하기

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