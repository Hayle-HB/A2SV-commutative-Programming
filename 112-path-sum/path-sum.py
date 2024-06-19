# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node, curr):
            if node and not node.left and not node.right:
                return curr + node.val == targetSum
            if not node:
                return False
            left = dfs(node.left, curr + node.val)
            right = dfs(node.right, curr +  node.val)

            return left or right
        
        return dfs(root, 0)