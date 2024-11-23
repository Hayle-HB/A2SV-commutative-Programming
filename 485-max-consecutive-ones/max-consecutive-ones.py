class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left, max_len = 0, 0

        curr_len = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                curr_len += 1
            
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0
        max_len = max(max_len, curr_len)
        return max_len