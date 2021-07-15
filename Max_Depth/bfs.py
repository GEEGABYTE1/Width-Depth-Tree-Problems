from Tree import Tree
from collections import deque

def bfs(root, count=0):
    path_queue = deque()
    initial_path = [root]
    path_queue.appendleft(initial_path)

    while path_queue:
        if count == 0 or len(path_queue) == 2:
            count += 1
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print('Traversing Node with Value: {}'.format(current_node.value))
        
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)
    
    return count







