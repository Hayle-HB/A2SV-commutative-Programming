# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        

        stack = [(p, q)]


        while stack:

            a, b = stack.pop()


            if not a and not b:
                continue
            
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            

            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        return True

        