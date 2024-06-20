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
        to_left = False

        queue = deque([root, None])

        result = []
        curr_lev = []

        while queue:
            curr = queue.popleft()

            if curr == None:
                if to_left:
                    result.append(curr_lev[::-1])
                    to_left = False
                else:
                    result.append(curr_lev)   
                    to_left = True
                curr_lev = []

                if queue:
                    queue.append(None)
            else:
                curr_lev.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

        return result

