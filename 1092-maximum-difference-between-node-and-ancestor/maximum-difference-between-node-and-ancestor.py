# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, Min, Max):
            if not node:
                return 0
            
            Min = min(Min, node.val)
            Max = max(Max, node.val)
            
            diff = abs(Min - Max)

            left = helper(node.left, Min, Max)
            right = helper(node.right, Min, Max)
            
            return max(diff, left, right)
        
        if not root:
            return 0
        
        Min = root.val
        Max = root.val
        
        return helper(root, Min, Max)
