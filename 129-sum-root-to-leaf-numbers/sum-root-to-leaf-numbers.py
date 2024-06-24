# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        answer = 0

        def dfs(node, curr):
            nonlocal answer
            if not node:
                return None
            curr += str(node.val)
            if not node.left and not node.right:
                 answer += int(curr)
                 return
            
            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, "")
        return answer