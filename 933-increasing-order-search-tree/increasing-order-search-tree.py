# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        current = root
        stack = []
        dummy = TreeNode(0)  
        prev = dummy  
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            prev.right = current  
            current.left = None 
            prev = current  

            current = current.right

        return dummy.right 
