class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        dic = {}
        left, right, Max = 0, 0, 0

        for right in range(len(nums)):
            dic[nums[right]]  = dic.get(nums[right], 0) + 1

            while dic[nums[right]] > k:
                dic[nums[left]] -= 1
                left += 1
            Max = max(Max, right - left + 1)
        return Max

        