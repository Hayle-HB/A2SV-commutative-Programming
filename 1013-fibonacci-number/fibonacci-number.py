class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        
        def help(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = help(n-2) + help(n-1)
                return memo[n]
        
        return help(n)

