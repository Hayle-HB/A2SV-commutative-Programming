class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: TreeNode, start: int, ans: list) -> int:
        if not root:
            return 0
        
        left = self.dfs(root.left, start, ans)
        right = self.dfs(root.right, start, ans)
        
        if root.val == start:
            ans[0] = max(left, right)
            return -1
        elif left >= 0 and right >= 0:
            return max(left, right) + 1
        else:
            ans[0] = max(ans[0], abs(left) + abs(right))
            return min(left, right) - 1
    
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        ans = [0]
        self.dfs(root, start, ans)
        return ans[0]