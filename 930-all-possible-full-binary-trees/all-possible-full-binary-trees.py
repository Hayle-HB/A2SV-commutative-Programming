# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        memo = {}


        def dp(n):
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                return []
            ans = []
            for left in range(1, n, 2):
                right = n - left - 1

                left_tree = dp(left)
                right_tree = dp(right)

     
                for l in left_tree:
                    for r in right_tree:
                        ans.append(TreeNode(0, l, r))
            memo[n] = ans
            return ans
        return dp(n)
        