""" Linked List Data Structure in Python """

class Node():
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class SlinkedList():
    def __init__(self):
        self.head = None

    def printlist(self):
        curr_head = self.head
        while curr_head != None:
            print(curr_head.data)
            curr_head = curr_head.next

    def insert_beginning(self,val):
        self.head = Node(val, self.head)

list = SlinkedList()
list.head = Node('Monday')
list.head.next = Node('Tuesday')
list.printlist()

print("\n")

list.insert_beginning('Sunday')
list.printlist()
