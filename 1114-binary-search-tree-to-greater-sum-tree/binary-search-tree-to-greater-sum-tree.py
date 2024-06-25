# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        greater = 0
        def dfs(node):
            nonlocal greater
            if not node:
                return None
            
            l = dfs(node.right)
            greater += node.val
            node.val = greater
            r = dfs(node.left)
        dfs(root)
        return root