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