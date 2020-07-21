class Node():
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class SlinkedList():
    def __init__(self, data = None, next = None, prev = None):
        self.head = Node(data, next, prev)
        self.tail = self.head

    def printlistf(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

    def printlistb(self):
        curr_node = self.tail
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.prev

    def insert_beginning(self, val):
        self.head.prev = Node(val, self.head)
        self.head = self.head.prev

    def insert_between(self, middle_node, val):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        if middle_node.next is not None:
            middle_node.next.prev = Node(val, middle_node.next, middle_node)
            middle_node.next = middle_node.next.prev
        else:
            self.insert_end(val)

    def insert_end(self, val):
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head

        curr_node = self.tail
        curr_node.next = Node(val, None, curr_node)
        self.tail = curr_node.next

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
list.head.data = 'Monday'
list.printlistf()
print("\n")

#  Inserting a new node at the head of the linked list
list.insert_beginning('Sunday')
list.printlistf()
print("\n")

# Inserting a new node at the end of the linked list
list.insert_end('Tuesday')
list.printlistf()
print("\n")

# inserting a new node in inserting inbetween two nodes
list.insert_between(list.head.next,'6')
list.printlistf()
print("\n")

list.printlistb()
print("\n")

# removing a node with a specific value
list.remove_node('6')
list.printlistf()
print("\n")

list.printlistb()
print("\n")
