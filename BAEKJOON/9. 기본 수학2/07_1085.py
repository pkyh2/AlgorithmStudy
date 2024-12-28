# 직사각형에서 탈출

'''
(0, 0)에서 (w, h)의 길이의 직사각형안에 (x, y)에서 직사각형의 경계까지가는 최소거리를 구하시오.
'''

# 풀이1
# (x, y)에서 각 변까지의 거리를 구해 크기 비교

x, y, w, h = map(int, input().split())
distance = []

if (x >= 1 and x <= w-1) or (y >= 1 and y <= h-1):
    distance.append(x)
    distance.append(y)
    distance.append(w - x)
    distance.append(h - y)

print(min(distance))

# 29200KB 76ms