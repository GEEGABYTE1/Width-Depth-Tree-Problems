# Problem 

Given a binary tree, find its maximum depth

Input: 3
     /   \
    9     20
          / \
        15   7

Output: 3 


# Solution 

Used the breadth-first search to count the amount of times it went down a layer. Bfs was an easier way to solve this problem as it would be much easier to keep count of the times it goes a layer down, due to it's behaviour of moving laterally. 

Time Complexity: `O(n)`


# More Information

`test.py` are test cases
`Tree.py` is the underlying tree data structure that needed to be used for the problem 

Made in Python 🐍
