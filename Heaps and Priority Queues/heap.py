class node():
    """docstring for node."""
    def __init__(self,data = None, parent = None):
        self.data = data
        self.parent = parent
        self.child1 = None
        self.child2 = None

class heap():
    def __init__(self):
        self.head = node()
        self.inser = self.head

    def add(self, data):
        if self.head.data == None:
            self.head.data = data
        else:
            if self.inser.child1 == None:
                self.inser.child1 = node(data, self.inser)
            else:
                self.inser.child2 = node(data, self.inser)

    
