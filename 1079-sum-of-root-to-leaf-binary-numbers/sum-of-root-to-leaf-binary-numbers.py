# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans  = 0

        def dfs(node, curr):
            if not node:
                return 0
            
            curr = (curr << 1) | node.val

            if not node.left and not node.right:
                return curr

            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left + right
        return dfs(root, 0)
        