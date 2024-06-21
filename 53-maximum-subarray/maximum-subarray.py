class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_curr = nums[0]

        for i in range(1, len(nums)):
            max_curr = max(max_curr + nums[i], nums[i])
            max_sum = max(max_sum, max_curr)
        
        return max_sum
        