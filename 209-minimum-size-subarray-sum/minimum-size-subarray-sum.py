class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums)+1

        left = 0
        right = 0
        Sum = 0
        for right in range(len(nums)):
            Sum += nums[right]

            while Sum >= target:
                min_len = min(min_len, right - left + 1)
                Sum -= nums[left]
                left += 1
            
        if min_len != (len(nums)+1):
            return min_len
        return 0
        