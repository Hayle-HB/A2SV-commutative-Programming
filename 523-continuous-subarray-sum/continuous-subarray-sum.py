class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix = {0:-1}

        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            reminder = curr % k if k != 0 else curr
            if reminder in prefix:
                if right - prefix[reminder] > 1:
                    return True
            
            if reminder not in prefix:
                prefix[reminder] = right
        return False