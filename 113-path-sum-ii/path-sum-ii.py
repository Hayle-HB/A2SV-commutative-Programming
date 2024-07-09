# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(node, curr, path):
            if not node:
                return []
            
            curr = curr + node.val
            path = path + [node.val]

            if not node.left and not node.right:
                if targetSum == curr:
                    answer.append(path)
            
            left = dfs(node.left, curr, path)
            right = dfs(node.right, curr, path)


            return left + right
        
        dfs(root, 0, [])
        return answer

            




       