# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def ite(root):

            stack = [root]
            ans = []

            while stack:
                curr = stack.pop()
                ans.append(curr.val)

                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)

            return ans 

        def dfs(root):
            if root == None:
                return []
            
            return dfs(root.left) + [root.val] + dfs(root.right)

        


        return dfs(root)
        