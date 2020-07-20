""" Linked List Data Structure in Python """

class Node():
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class SlinkedList():
    def __init__(self):
        self.head = None

    def printlist(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

    def insert_beginning(self, val):
        self.head = Node(val, self.head)

    def insert_between(self, middle_node, val):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        middle_node.next = Node(val, middle_node.next)

    def insert_end(self, val):
        if self.head == None:
            self.head = Node(val)

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(val, next = None)


list = SlinkedList()
list.head = Node('Monday')
list.head.next = Node('Tuesday')
list.printlist()
print("\n")

list.insert_beginning('Sunday')
list.printlist()
print("\n")

list.insert_end('Wednesday')
list.printlist()
print("\n")

list.insert_between(list.head.next,'6')
list.printlist()
print("\n")
