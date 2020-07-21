class Node():
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

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

        middle_node.next.prev = Node(val, middle_node.next, middle_node)
        middle_node.next = middle_node.next.prev

    def insert_end(self, val):
        if self.head == None:
            self.head = Node(val)

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = Node(val, next = None)

    def remove_node(self, val):
        curr_node= self.head
        if (curr_node is not None):
            if (curr_node.data == val):
                self.head = curr_node.next
                curr_node = None
                return

        while (curr_node is not None):
            if curr_node.data == val:
                break
            prev_node = curr_node
            curr_node = curr_node.next

        if (curr_node == None):
            return

        prev_node.next = curr_node.next
        curr_node = None


# creating a linked list and intializing the head.
list = SlinkedList()
list.head = Node('Monday')
list.printlist()
print("\n")

#  Inserting a new node at the head of the linked list
list.insert_beginning('Sunday')
list.printlist()
print("\n")

# Inserting a new node at the end of the linked list
list.insert_end('Tuesday')
list.printlist()
print("\n")

# inserting a new node in inserting inbetween two nodes
list.insert_between(list.head.next,'6')
list.printlist()
print("\n")

# removing a node with a specific value
list.remove_node('6')
list.printlist()
print("\n")
