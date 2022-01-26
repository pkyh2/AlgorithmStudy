# 트리의 부모 찾기
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

'''
        1
    4       6
  2   7       3
            5
'''

import sys
input = sys.stdin.readline
node = int(input())
tree = [[] for i in range(node+1)]    # node + 1개 만큼의 빈 2차원 배열 선언
parent = [[] for i in range(node+1)]

# 트리구조 생성 [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4] ]
for _ in range(node - 1):
    i, j = map(int, input().split())
    tree[i].append(j) # 그래프 생성
    tree[j].append(i)

def dfs(tree, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()

        for i in tree[node]:    # 1번째 노드와 연결되어있는 수
            parent[i].append(node)  # [i]번째 부모는 node
            stack.append(i)
            tree[i].remove(node)    # 부모노드를 제거
    return parent   # 부모노드만 있는 2차원리스트

for i in list(dfs(tree, 1, parent))[2:]:
    print(i[0])

# 55496 456