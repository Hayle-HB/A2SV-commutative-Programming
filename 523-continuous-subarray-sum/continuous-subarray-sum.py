class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = 0
        prefix = {0: -1}  
        
        for idx, num in enumerate(nums):
            pre_sum += num
            remainder = pre_sum % k if k != 0 else pre_sum
            
            if remainder in prefix:
                if idx - prefix[remainder] > 1:
                    return True
            else:
                prefix[remainder] = idx
        
        return False
