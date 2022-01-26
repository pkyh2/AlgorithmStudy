# 노드 클래스 생성
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):			# 루트 노드를 인자로 받아온다.
    print(node.data, end='')	# 부모 노드 출력
    if node.left_node != '.':	# 부모 노드의 왼쪽 노드가 != '.'면 
        pre_order(tree[node.left_node])		# 그 노드를 부모 노드로 다시 pre_order함수 실행
    if node.right_node != '.':				# 왼쪽 노드가 '.'이면 오른쪽 노드를 검사
        pre_order(tree[node.right_node])	# 오른쪽 노드를 부모 노드로 해서 pre_order함수 실행
        
# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())	# 트리의 크기 입력
tree = {}			# dict 구조
# A ~ G까지 루트 노드부터 왼쪽 -> 오른쪽으로 트리가 2차수인 트리 생성
for i in range(n):
    data, left_node, right_node = input().split()	#부모 노드, 자식 노드1, 자식 노드2 입력
    # 자식 노드가 없으면 None
    if left_node == ".":
        left_node = '.'
    if right_node == ".":
        right_node = '.'
    # 트리객체에 노드 삽입
    tree[data] = Node(data, left_node, right_node)
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

# 30860 72