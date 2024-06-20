# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        to_left = False #we can utilize this variable to make the turn to the left and right but we can also reverse after we get the answer

        queue = deque([root, None])

        result = []
        curr_lev = []

        while queue:
            curr = queue.popleft()

            if curr == None:
                result.append(curr_lev)
                curr_lev = []

                if queue:
                    queue.append(None)
            else:
                curr_lev.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
        
        for i in range(1, len(result), 2):
            result[i] = result[i][::-1]
        return result

