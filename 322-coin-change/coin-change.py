class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        memo = {}


        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            

            result = float('inf')


            for coin in coins:
                if coin <= rem:
                    result = min(result, dp(rem - coin) + 1)
            memo[rem] = result
            return result
        r = dp(amount)
        return r if r != float('inf') else -1