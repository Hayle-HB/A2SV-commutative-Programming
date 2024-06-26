# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, parent, grapa):
            nonlocal ans
            if not node:
                return 0
            
            if grapa and grapa.val % 2 == 0:
                ans += node.val
            
            if node.left:
                dfs(node.left, node, parent)
            if node.right:
                dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return ans