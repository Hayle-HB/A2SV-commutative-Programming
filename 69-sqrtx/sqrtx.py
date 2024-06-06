class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return low-1
            
        