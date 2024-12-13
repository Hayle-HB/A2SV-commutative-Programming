class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)


        prefix[0] = nums[0]
        less = nums[0] < 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            if prefix[i] < 1:
                less = True

        return -(min(prefix)-1) if less else 1
       
        