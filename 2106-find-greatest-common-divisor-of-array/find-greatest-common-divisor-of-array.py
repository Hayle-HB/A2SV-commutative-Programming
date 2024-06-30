class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        return gcd(large, small)

        