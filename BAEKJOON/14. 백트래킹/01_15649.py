# N과 M(1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):     # 1 ~ 4
        if i not in s:
            s.append(i)         # [2, ]
            dfs()
            s.pop()

dfs()
# 30864 216

# 순열함수
from itertools import permutations
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)
for i in P:
    print(' '.join(map(str, i)))