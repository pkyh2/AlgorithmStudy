# N과 M(2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []
def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))

    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)
# 30864 64

# 조합
from itertools import combinations
N, M = map(int, input().split())
C = combinations(range(1, N+1), M)
for i in C:
    print(' '.join(map(str, i)))