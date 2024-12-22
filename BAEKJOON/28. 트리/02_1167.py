import sys
from collections import deque
input = sys.stdin.readline

V = int(input())

treeInfo = [[] for _ in range(V+1)]

for _ in range(V):
    info = list(map(int, input().split()))
    for i in range(1, len(info)-1, 2):
        treeInfo[info[0]].append((info[i], info[i+1]))

def bfs(node):
    visited = [-1] * (V+1)

    q = deque()
    q.append(node)
    visited[node] = 0

    _max = [0, 0]

    while q:
        old = q.popleft()
        for new in treeInfo[old]:
            if visited[new[0]] == -1:
                visited[new[0]] = visited[old] + new[1]
                q.append(new[0])

                if _max[0] < visited[new[0]]:
                    _max[0] = visited[new[0]]
                    _max[1] = new[0]
    return _max

dis1, node1 = bfs(1)
result, node2 = bfs(node1)

print(result)
# 70368 660