# 노드 생성 클래스
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

# 링크드 리스트 클래스
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    # 인자로 pos가 주어지면, 
    def getAt(self, pos):
        # pos가 0이거나 전체 노드개수 보다 많으면
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        # pos번까지 반복
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        # 헤드를 담는 변수 선언
        curr = self.head

        # 링크드 리스트가 없으면
        if curr == None:
            return []

        # 값을 담을 리스트 빈 리스트 선언
        linkedList = []

        # 현재 값이 있으면 계속 반복
        while curr != None:
            # 현재 값을 리스트에 추가
            linkedList.append(curr.data)
            # 다음 연결 리스트로 이동
            curr = curr.next

        return linkedList



# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0



# 노드 삽입 클래스
def insertAt(self, pos, newNode):
    # 리스트 범위를 벗어났을때
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    # 첫번째 노드에 삽입할 때
    if pos == 1:
        newNode.next = self.head
        self.head = newNode

    else:
        prev = self.getAt(pos - 1)
        newNode.next = prev.next
        prev.next = newNode
    
    if pos == self.nodeCount+1:
        self.tail = newNode
    
    self.nodeCount += 1
    return True
    