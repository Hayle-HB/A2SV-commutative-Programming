# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}

        def inorder(node):
            if not node:
                return None
            if node.val not in dic:
                dic[node.val] = 1
            else:
                dic[node.val] = dic.get(node.val, 0) + 1
            
            inorder(node.left)
            inorder(node.right)
        
        inorder(root)

        max_count = max(dic.values())
        result = []
        for node_value in dic:
            if dic[node_value] == max_count:
                result.append(node_value)


        return result
        