class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            else:
                result = helper(n - 1) + helper(n - 2) + helper(n - 3)
                memo[n] = result
                return result
        
        return helper(n)