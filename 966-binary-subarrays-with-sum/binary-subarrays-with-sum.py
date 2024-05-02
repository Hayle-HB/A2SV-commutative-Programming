class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0:1}

        Sum = 0
        count = 0
        for right in range(len(nums)):
            Sum += nums[right]
            comp = Sum - goal

            if comp in prefix:
                count += prefix[comp]
            prefix[Sum] = prefix.get(Sum, 0) + 1
        
        return count