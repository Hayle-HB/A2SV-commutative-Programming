class Solution:
    def arrangeCoins(self, n: int) -> int:

        total = 0
        k = 1
        stair  = 1
        while stair <= n:
            total += 1
            k += 1
            stair += k
        return total


        