# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root, None])
        answer = []

        curr_lev = []

        while queue:
            curr = queue.popleft()

            if curr == None:
                answer.append(curr_lev)
                curr_lev = []
                if queue:
                    queue.append(None)
            else:
                curr_lev.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        

        return answer

        