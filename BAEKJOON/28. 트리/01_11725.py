# 트리의 부모 찾기

import sys

node = int(input()) # 노드의 개수 입력
node_graph = [[] for _ in range(node + 1)] # 노드 개수 + 1개만큼 빈 리스트 생성 [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4] ]
parent = [[] for _ in range(node + 1)]

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())   # 문제 입력값을 입력받는다.
    node_graph[i].append(j)
    node_graph[j].append(i)

# 그래프의 형태
'''
        1
    4       6
  2   7       3
            5
'''

#DFS나 BFS나 무관

def dfs(graph_list, start, parent):
    # 스택에 루트 노드를 넣는다.
    stack = [start]
    
    while stack:
        # node변수에 루트 노드(1)를 대입
        node = stack.pop()
        # (1)번 원소[6, 4]를 반복
        for i in graph_list[node]:  # [6, 4], [1, 3], 1[4], [2, 7]
            #2차원 parent에 i번째 index에 1대입
            parent[i].append(node)  # i == 6 -> parent[6].append(1), i==1 -> parent[1].append(6), i==4 -> parent[4].append[1], i==2 -> parend[2].append(4)
            # 스택에 6, 4 대입
            stack.append(i) # [6][1][4]
            graph_list[i].remove(node)  # 6번째 index [1, 3] 에서 1제거, 1번째 index [6, 4]에서 6제거, 4index [1,2,7] 1제거
    return parent

# def 함수의 인자값으로 트리 그래프와 루트노드, 부모노드가 담길 리스트를 넣어준다.
for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])