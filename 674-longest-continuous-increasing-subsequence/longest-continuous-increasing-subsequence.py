class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count, curr = 0  , 0

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                curr += 1
            else:
                count = max(count, curr)
                curr = 0
        count = max(count, curr)
        return count + 1
        