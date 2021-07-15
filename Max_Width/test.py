from tree import TreeNode 
from dfs import dfs 
from dfs import width_counter

tree_node1 = TreeNode(1)
tree_node2 = TreeNode(2)
tree_node3 = TreeNode(3)
tree_node4 = TreeNode(4)
tree_node5 = TreeNode(5)
tree_node6 = TreeNode(6)
tree_node7 = TreeNode(7)
tree_node8 = TreeNode(8)

tree_node1.add_child(tree_node2)
tree_node1.add_child(tree_node3)
tree_node2.add_child(tree_node4)
tree_node2.add_child(tree_node5)
tree_node3.add_child(tree_node8)
tree_node8.add_child(tree_node6)
tree_node8.add_child(tree_node7)

goal_path = dfs(tree_node1, 7)

print(width_counter(goal_path))