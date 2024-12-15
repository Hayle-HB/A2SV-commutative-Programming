class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if x == sum(nums):
            return len(nums)
        left, max_len = 0, -1
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]

            while left < right and curr > target:
                curr -= nums[left]
                left += 1
            if curr == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len  if max_len != -1 else -1
            
        