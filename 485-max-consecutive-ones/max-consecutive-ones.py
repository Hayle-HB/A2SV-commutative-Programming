class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        curr = 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                curr += 1
            else:
                count = max(curr, count)
                curr = 0
        count = max(count, curr)
        return count
      