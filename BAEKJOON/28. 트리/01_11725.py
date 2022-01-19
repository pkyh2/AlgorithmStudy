# 트리의 부모 찾기

import sys

node = int(input()) # 노드의 개수 입력
node_graph = [[] for _ in range(node + 1)] # 노드 개수 + 1개만큼 빈 리스트 생성 [[], [6, 4], [4, ], [6, 5], [1, 2, 7], [3], [1, 3], [4] ]
parent = [[] for _ in range(node + 1)]

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())   # 문제 입력값을 입력받는다.
    node_graph[i].append(j) # 
    node_graph[j].append(i)

#DFS나 BFS나 무관

def dfs(graph_list, start, parent):
    # 스택에 루트 노드를 넣는다.
    stack = [start]
    
    while stack:
        # node변수에 루트 노드(1)를 대입
        node = stack.pop()
        # (1)번 원소[6, 4]를 반복
        for i in graph_list[node]:
            #2차원 parent에 i번째 index에 1대입
            parent[i].append(node)
            # 스택에 6, 4 대입
            stack.append(i)
            graph_list[i].remove(node)
    return parent

# def 함수의 인자값으로 트리 그래프와 루트노드, 부모노드가 담길 리스트를 넣어준다.
for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])