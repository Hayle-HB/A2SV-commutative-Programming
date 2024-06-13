# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_width = 0
        
        def backtrack(node: TreeNode, depth: int, position: int, levels: dict):
            if not node:
                return
            
            if depth not in levels:
                levels[depth] = position
            
            self.max_width = max(self.max_width, position - levels[depth] + 1)
            
            backtrack(node.left, depth + 1, 2 * position, levels)
            backtrack(node.right, depth + 1, 2 * position + 1, levels)
        
        levels = {}
        backtrack(root, 0, 0, levels)
        
        return self.max_width
