class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, c
        while l <= r:
            mid = (l + r)//2
            if mid * mid == c: 
                return True
            elif mid * mid > c: 
                r = mid - 1
            else: 
                l = mid + 1

        low, high = 0, l - 1

        while low <= high:
            mid = low * low + high * high
            if mid == c: 
                return True
            elif mid > c:
                 high -= 1
            else: 
                low += 1
        return False