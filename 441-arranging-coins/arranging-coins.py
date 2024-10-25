class Solution:
    def arrangeCoins(self, n: int) -> int:

        l = 0
        r = n

        while l <= r:
            mid = l + (r-l) // 2
            k = mid * (mid + 1)  // 2

            if k == n:
                return mid
            elif k < n:
                l = mid+1
            else:
                r = mid - 1
        return r
        



        