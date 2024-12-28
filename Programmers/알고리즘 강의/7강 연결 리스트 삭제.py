class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return IndexError

        curr = self.getAt(pos)

        if pos == 1 and self.nodeCount == 1:
            self.head = None
            self.tail = None

        # 노드가 유일하지 않은데 맨처음 노드를 삭제하려면
        # head를 다음 노드로 변경해준다.
        elif pos == 1:
            self.head = self.getAt(pos+1)
        
        else:
            prev = self.getAt(pos - 1)

            if pos != self.nodeCount:
                prev.next = self.getAt(pos+1)
            else:
                self.tail = prev
                prev.next = None
        
        self.nodeCount -= 1
        return curr.data
            
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0