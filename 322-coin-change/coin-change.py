class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(rem):
            if rem == 0:
                return 0
            
            if rem in memo:
                return memo[rem]
            
            result = float('inf')
            for coin in coins:
                if coin <= rem:
                    result = min(result, dp(rem - coin)+1)
            
            memo[rem]  = result
            return memo[rem]
        
        r = dp(amount)
        if r == float('inf'):
            return -1
        return r
        
