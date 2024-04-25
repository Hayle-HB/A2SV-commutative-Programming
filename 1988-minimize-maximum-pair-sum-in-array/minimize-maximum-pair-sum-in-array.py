class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        Max = nums[0] + nums[-1]

        for i in range(len(nums)//2):
            Max = max(nums[i] + nums[-i-1], Max)
        return Max
        