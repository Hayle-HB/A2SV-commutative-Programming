class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # if n is even the solution will be pow(4*5, n/2) else pow(4*5, n/2 * 5)
            MOD = 10 ** 9 + 7
            good, x = 5 ** (n % 2), 4 * 5
            
            h = n // 2
            while h != 0:
                if h % 2 == 1: #if it is even
                    good = good * x % MOD
                x = x * x % MOD
                h //= 2
            return good

        