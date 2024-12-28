import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for i in range(N+1)]       # [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
parent = [[0] for i in range(N+1)]

for _ in range(N-1):
    i, j = map(int, input().split())    # 트리 입력

    # 트리 생성
    tree[i].append(j)
    tree[j].append(i)

# 풀이1(반복문)
def dfs(tree, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()  # 스택에 처음 들어온 값을 노드에 집어 넣고

        for i in tree[node]:
            parent[i].append(node)  # 노드 6의 부모노드는 1번이다. 추가
            stack.append(i)         # 6번 노드가 부모 노드가 되어 자식노드를 찾는다.
            tree[i].remove(node)       # 1번 노드는 6번노드의 부모노드이기 때문에 1번이 6번의 자식노드가 될 수 없기 때문에 제거

    return parent

for i in list(dfs(tree, 1, parent)[2:]):
    print(i[0])
# 55496 456

# 풀이2(재귀)
def dfs(tree, start, parent):
    for i in tree[start]:
        if parent[i] == [0]:
            parent[i].append(start)
            dfs(tree, i, parent)

dfs(tree, 1, parent)
for i in parent[2:]:
    print(i[1])
# 170280 512