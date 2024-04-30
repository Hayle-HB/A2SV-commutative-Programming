class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prefix_sums = {0: -1}  
        
        for idx, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k if k != 0 else prefix_sum
            
            if remainder in prefix_sums:
                if idx - prefix_sums[remainder] > 1:
                    return True
            else:
                prefix_sums[remainder] = idx
        
        return False
