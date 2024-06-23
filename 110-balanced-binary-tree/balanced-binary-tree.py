# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0, True
            
            left, left_bal = dfs(node.left)
            right, right_bal = dfs(node.right)
            height = max(left, right) + 1
            curr = left_bal and right_bal and abs(right-left) <=  1

            return height, curr
        
        _, answer = dfs(root)
        return answer

        
        