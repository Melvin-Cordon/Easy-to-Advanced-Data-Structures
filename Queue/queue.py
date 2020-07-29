""" Stack Data Structure in Python """

class Node():
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class queueD():
    def __init__(self):
        self.front = None
        self.back = None

    def printlist(self):
        curr_node = self.front
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next

    def queue(self, val):
        if self.front == None:
            self.front = Node(val)
            self.back = self.front
            return

        self.back.next = Node(val)
        self.back = self.back.next

    def dequeue(self):
        curr_node = self.front
        self.front = curr_node.next
        curr_node = None

line = queueD()

line.queue("1")
line.printlist()
print('\n')

line.queue("2")
line.queue("3")
line.queue("4")
line.queue("5")
line.printlist()
print('\n')

line.dequeue()
line.printlist()
print('\n')

line.dequeue()
line.dequeue()
line.printlist()
print('\n')
