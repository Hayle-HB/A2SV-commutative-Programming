# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True

        def dfs(node):
            if not node:
                return True
            
            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l-r) > 1:
                self.answer = False
            
            return 1 + max(l, r)
        
        dfs(root)
        return self.answer
        