class Node():
    def __init__(self):
        self.data = None
        self.link = None

a = Node()
a.data = 1
b = Node()
b.data = 2
c = Node()
c.data = 3
d = Node()
d.data = 4

a.link = b
b.link = c

class LinkedList():
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        curr = self.head
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        while i < pos:
            curr = curr.link
            i += 1
        return curr

    def traverse(self):
        curr = self.head
        linkedlist = []
        while self.nodeCount != 0:
            linkedlist.append(curr.data)
            curr = curr.link
            print(self.nodeCount)
            self.nodeCount -= 1
        return linkedlist

    def insertAt(self, pos, newNode):
        # 노드 개수 예외처리
        if pos < 1 and pos > self.nodeCount + 1:
            return False
        
        # pos가 1일때는 newNode가 head가 된다.
        if pos == 1:
            newNode.link = self.head
            self.head = newNode
        else:
            # prev가 tail이 되니까
            if pos == self.nodeCount + 1:
                pre = self.tail
            # prev가 pos-1에 위치하니까
            else:
                pre = self.getAt(pos-1)
            newNode.link = pre.link
            pre.link = newNode
                
            # # pos, pos-1 객체 찾기
            # curr = self.getAt(pos)
            # pre = self.getAt(pos-1)

            # # newNode의 link를 찾은 객체에 연결
            # newNode.link = curr
            # pre.link = newNode

        self.nodeCount += 1
        return True

    def popAt(self, pos):
        if pos < 1 and pos > self.nodeCount:
            return IndexError
        curr = self.getAt(pos)
        if pos == 1 and self.nodeCount == 1:
            self.head = None
            self.tail = None

        if pos == 1:
            self.head = self.getAt(pos+1)
        else:
            pre = self.getAt(pos-1)
            if pos != self.nodeCount:
                # link에 다음 객체를 대입
                pre.link = self.getAt(pos+1)
            else:
                # 이전 객체 다음에 객체가 없으면 None
                self.tail = pre
                pre.link = None

        self.nodeCount -= 1
        return curr.data

list1 = LinkedList()
list1.nodeCount = 3
list1.head = a
list1.tail = c
list1.insertAt(4, d)
print(list1.getAt(2))
print(list1.traverse())

# print(list1.head.link.data)
print(list1.tail)
print(list1.popAt(3))