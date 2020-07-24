""" Stack Data Structure in Python """

class Node():
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class stack():
    def __init__(self):
        self.head = None

    def printlist(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

    def push(self, val):
        self.head = Node(val, self.head)

    def pop(self):
        curr_node = self.head
        self.head = curr_node.next
        curr_node = None

        return

train = stack()
train.push(1)
train.push(2)
train.push(3)
train.push(4)
train.printlist()
print("\n")

train.pop()
train.printlist()
print("\n")

train.pop()
train.pop()
train.printlist()
print("\n")
