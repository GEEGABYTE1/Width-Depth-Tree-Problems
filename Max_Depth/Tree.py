class Tree:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, new_child):
        self.children.append(new_child)

    def remove_child(self, child):
        self.children = [i for i in self.children if not i == child]
    
    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.value)
            nodes += current_node.children