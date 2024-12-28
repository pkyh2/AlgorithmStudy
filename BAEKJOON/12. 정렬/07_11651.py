# 좌표 정렬하기2

# 풀이2
# sorted(key=) 를 이용한 해결법

import sys
input = sys.stdin.readline

N = int(input())
point = []
for i in range(N):
    xy = list(map(int, input().split()))
    point.append(xy)

point = sorted(point, key=lambda x: (x[1], x[0]))
for i in point:
    for j in i:
        print(j, end=' ')
    print()
    
# 57672 472