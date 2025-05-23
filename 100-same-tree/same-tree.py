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


            l, r = stack.pop()


            if l.left and r.left:
                stack.append((l.left, r.left))
            
            if l.left or r.left:
                if not l.left:
                    return False
                if not r.left:
                    return False
            if l.right or r.right:
                if not l.right:
                    return False
                if not r.right:
                    return False
            
            if l.right and r.right:
                stack.append((l.right, r.right))
            if l.val != r.val:
                return False

        return True
            
        