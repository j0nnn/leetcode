# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root: return None
        memory = {}

        # dfs search for traversing through the tree. saving non-visited nodes to a hashmap
        def traverse(node):
            if not node:
                return
            if node in memory:
                return
            memory[node] = NodeCopy(node.val)
            traverse(node.left)
            traverse(node.right)
            traverse(node.random)
        
        # traverse entire tree
        traverse(root)
        
        # update values in copied nodes to match the corresponding copied nodes
        for node, copy in memory.items():
            if node.right: copy.right = memory[node.right]
            if node.left: copy.left = memory[node.left]
            if node.random: copy.random = memory[node.random]
        return memory[root]
        