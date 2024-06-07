# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

            def backtrack(node,path, rst):
                chiled = (node.left, node.right)
                path.append(str(node.val))
                if not any(chiled):
                    rst.append('->'.join(path))
                
                for child in filter(None, chiled):
                    backtrack(child, path, rst)
                path.pop()
                return rst
            
            return backtrack(root, [], [])
