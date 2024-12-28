import sys
from collections import deque
input = sys.stdin.readline

# 정점의 개수
V = int(input())

# 각 인덱스가 정점
# 원소로는 그 인덱스와 연결된 정점과, 거리
treeInfo = [[] for _ in range(V+1)]     # 정점이 1번부터 시작하여 V+1개 만큼 생성

# 트리정보 입력, 정점 개수만큼 반복
for _ in range(V):
    # 정보 입력
    info = list(map(int, input().split()))  # ex)4, 2, 4, 3, 3, 5, 6, -1
    
    # 첫번째 원소는 정점이고, 마지막 원소는 -1이니까 제외하고 반복
    for i in range(1, len(info)-1, 2):
        # treeInfo에 info의 첫번째 원소(정점)에 해당하는 인덱스에
        # 연결된 정점과, 거리를 tuple형태로 append해준다.
        treeInfo[info[0]].append((info[i], info[i+1]))

#---------------트리구조생성완료-----------------

'''
트리의 지름 구하는 방법
1. 트리의 지름은 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
2. 임의의 노드x(보통 루트노드1)를 잡는다. -> bfs(1)
3. 노드 x에서 가장 먼 노드 a를 찾는다.
4. 노드 a에서 가장 먼 노드 b를 찾는다.
'''

def bfs(node):
    # 방문처리 변수, 1 ~ V까지
    visited = [-1] * (V+1)

    # 큐에 첫 노드 삽입 후 방문처리
    q = deque()
    q.append(node)
    visited[node] = 0

    _max = [0, 0]   # 현재 가장 먼 노드까지의 거리, 그 노드의 위치

    # bfs 출발
    while q:
        old = q.popleft()   # 방문한 노드를 old에 대입
        for new in treeInfo[old]:   # 방문한 노드와 인접한 노드와 거리 출력
            # 인접한 노드가 방문한 노드가 아니라면
            if visited[new[0]] == -1:
                
                # 이전에 방문한 노드까지의 누적거리와 새로 방문하러간 노드까지의 거리를 더해준다.
                visited[new[0]] = visited[old] + new[1]
                
                # 그리고 큐에 새로 방문한 노드를 넣어준다.
                q.append(new[0])

                # 누적 거리 비교
                if _max[0] < visited[new[0]]:   # 현재 누적 거리와 / 방문한 노드까지의 거리의 누적거리를 비교
                    _max[0] = visited[new[0]]   # 누적거리를 갱신하고
                    _max[1] = new[0]            # 그 노드의 위치로 바꿔준다.
    return _max

# bfs에 루트노드를 넣고 가장 먼 정점의 거리와 위치를 return받는다.
dis1, node1 = bfs(1)

# node1를 bfs에 넣고 가장 먼 정점의 거리, 위치를 구한다.
result, node2 = bfs(node1)

print(result)
# 70368 660

'''
BFS 알고리즘
루트 노드에서 인접한 노드들을 먼저 탐색

DFS 알고리즘
루트 노드에서 인접한 노드를 탐색 후 그 간선으로 연결되어 있는 방향으로 끝까지 탐색
'''