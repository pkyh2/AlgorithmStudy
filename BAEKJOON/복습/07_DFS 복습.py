# DFS 개념 복습 겸
# 바이러스
'''
1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수

'''

import sys
input = sys.stdin.readline

# 정점의 개수
labtop = int(input())

# 그래프 구조 생성
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
graphInfo = [[] for _ in range(labtop+1)]

N = int(input())
for i in range(N):
    c1, c2 = map(int, input().split())
    graphInfo[c1].append(c2)
    graphInfo[c2].append(c1)
#------------------------------------------

visited = [0] * (labtop+1)
cnt = -1
def dfs(graph, start, visited):
    global cnt
    visited[start] = 1      # 방문 처리
    cnt += 1 

    for i in graph[start]:
        if not visited[i]:  # 참이 아니면, False 방문하지 않았으면
            dfs(graph, i, visited)
    
    return cnt

result = dfs(graphInfo, 1, visited)
print(result)
# 30860 68