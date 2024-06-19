class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        res = nums[0]
        Sum = nums[0]

        for i in range(1, len(nums)):
            Sum = Sum + nums[i]
            ave = ceil(Sum / (i  + 1))
            res = max(res, ave)
        return res
