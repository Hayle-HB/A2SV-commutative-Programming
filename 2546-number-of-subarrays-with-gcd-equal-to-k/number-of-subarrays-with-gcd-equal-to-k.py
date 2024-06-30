class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        count = 0

        for i in range(len(nums)):
            curr = 0 
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])
                if curr == k:
                    count += 1
                if curr < k:
                    break
        return count

                