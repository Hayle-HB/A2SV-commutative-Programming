class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low_range,high_range=float('-inf'),float('inf')

        def check(root,low_range,high_range):

            if root==None:
                return True

            if root.val<=low_range or root.val>=high_range:
                return False

            return check(root.left,low_range,root.val) and check(root.right,root.val,high_range)
            
        return check(root,low_range,high_range)