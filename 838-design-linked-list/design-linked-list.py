class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class MyLinkedList:


    def __init__(self, head=None):
        self.head = head
       


    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if cur == None:
                return -1
            cur = cur.next
        return cur.data if cur != None else -1


    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode


    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newnode


    def addAtIndex(self, index: int, val: int) -> None:
        newnode = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for i in range(index-1):
            if cur == None:
                return
            cur = cur.next
        newnode.next = cur.next
        cur.next = newnode




    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        for i in range(index-1):
            if cur == None:
                return
            cur = cur.next
        if cur != None and cur.next != None:
            cur.next = cur.next.next