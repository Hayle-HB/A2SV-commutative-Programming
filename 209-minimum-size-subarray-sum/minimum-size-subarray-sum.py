class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       
       curr_sum = 0
       min_len = len(nums)+1
       left = 0
       for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)

                curr_sum -= nums[left]
                left += 1
            
       return min_len if min_len != len(nums)+1 else 0

        
            

        