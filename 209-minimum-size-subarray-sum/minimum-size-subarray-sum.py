class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0

        curr = 0

        min_len = len(nums)+1


        for right in range(len(nums)):
            curr += nums[right]
            
            while  curr >= target:
                min_len = min(min_len, right - left + 1)
                curr -= nums[left]
                left += 1

            
        return min_len if min_len < len(nums)+1 else  0
        