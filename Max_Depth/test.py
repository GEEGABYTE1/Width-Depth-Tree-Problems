from Tree import Tree
from bfs import bfs

tree1 = Tree(3)
tree2 = Tree(9)
tree3 = Tree(20)
tree4 = Tree(15)
tree5 = Tree(7)

tree1.add_child(tree2)
tree1.add_child(tree3)
tree3.add_child(tree4)
tree3.add_child(tree5)

goal_queue = bfs(tree1)

print(goal_queue)
