# LeetCode 0707 - Design Linked List

class list_node(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList(object):
    def __init__(self):
        self.dummy = list_node(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size: return
        if index < 0 : index = 0
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        new_node = list_node(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size : return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
