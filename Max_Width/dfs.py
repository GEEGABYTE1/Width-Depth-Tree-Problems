from tree import TreeNode

def dfs(root_node, goal, path=(), layers_lst=[], root=None):
    if root == None:
        root = root_node
    path = path + (root_node,)
    current_level_lst=[]
    
    for i in path:
        if not i.value in current_level_lst:
            current_level_lst.append(i.value)


    for node in root_node.children:
        new_path = dfs(node, goal, path, layers_lst, root)
    
        if not new_path == None:
            return new_path 
    
    layers_lst.append(current_level_lst)

    
    last_lst = layers_lst[-1]
    if root.value == last_lst[-1]:
        return layers_lst 
    else:
        return None


def width_counter(lst):
    lst_lengths = []

    for list in lst:
        lst_lengths.append(len(list))
    
    max_layer = max(lst_lengths)

    layers = [[] for i  in range(max_layer)]

    

    for list in lst:
        index_counter = 0
        for val_index in range(len(list)):
            if val_index == index_counter:
                value = list[val_index]
                if not value in layers[index_counter]:
                    layers[index_counter].append(value)
                
                list[index_counter] = None
                index_counter += 1

    node_count = [len(i) for i in layers]
    return max(node_count)
                
                
            



