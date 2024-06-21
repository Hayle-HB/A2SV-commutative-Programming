class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        Min = nums[0]
        Max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            curr_min = min(curr_min + nums[i], nums[i])

            Min = min(Min, curr_min)
            Max = max(Max, curr_max)

        return max(abs(Min), Max)
        