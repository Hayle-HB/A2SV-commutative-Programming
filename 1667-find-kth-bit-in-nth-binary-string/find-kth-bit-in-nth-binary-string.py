class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k % 2 == 1:
            return str((k // 2) % 2)
        
        def helper(total, k):
            mid = (total + 1)//2
            if total == 1:
                return 1
            if k == mid:
                return 1
            if k > mid:
                return helper(total//2, mid - (k - mid)) ^ 1
            return helper(total//2, k)
        return str(helper(2**(n-1)-1, k//2))