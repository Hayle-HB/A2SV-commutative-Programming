class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, curr = 0, 1
        count = 0

        for right in range(len(nums)):
            curr *= nums[right]

            while left <= right and curr >= k:
                curr /= nums[left]
                left += 1
            count += right - left + 1
        
        return count