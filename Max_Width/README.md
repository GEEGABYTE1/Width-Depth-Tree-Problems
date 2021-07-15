# Max Width of Binary Tree

Problem: Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths of all levels.

Input: 1 -> [2, 3], 2 -> [4, 5], 3 -> 8, 8 -> [6, 7]

Output: 3

# Solution 

With the depth first search algorithm, I got all the permutations of each sequence. We then assume each index of the list represents a level. 

For example,
    Let [a, b, c] be a list of the returned permutations of our dfs algorithm. 

    Index(a) = Level 1 
    Index(b) = Level 2
    Index(c) = Level 3 

    We do this because dfs returns the depth of the traversed path. Hence, if the algorithm traverses each depth all the way to the leaf node, each path must be slight symmetrical to each other. 


We can prove this with our second function `.width_counter()`. With all the permutations formatted in one 2D array, we then split each element in each list based on indices. All the elements at index 0 will be placed in the list at index 0, and so on. This is called partioning, and after, we will see a returned array with sub-arrays with sorted elements based on indicies. We can double check if this is correct by simply comparing the tree diagram with the elements in our list. If each layer of the tree has the same nodes as each list in that very index (assuming again the indicies are levels), we know we have done it correct as our array is simply just the tree given. 

The last step is to compare the lengths of each array in the 2D array, and the largest array (the array with the biggest length) will be the biggest level. 


Time Complexity of dfs: `O(n)`
Time Complexity of function (`.()width_counter`): `O(n^2)`


# More Information 

- `test.py` are test inputs 
- `tree.py` is the underlying tree data structure used.
- Made in Python 🐍
