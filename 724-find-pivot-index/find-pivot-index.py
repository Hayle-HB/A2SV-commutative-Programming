class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        n = len(nums)
        right_sum[n-1] = nums[n-1]
        left_sum[0] = nums[0]
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i]
            right_sum[n-i-1] = right_sum[n-i] + nums[n-i-1]
        for i in range(n):
            if left_sum[i] == right_sum[i]:
                return i
        return -1


            

        
        
        
        