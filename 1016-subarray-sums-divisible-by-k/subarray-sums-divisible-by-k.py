class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}  
        total_sum = 0
        count = 0
        
        for right in range(len(nums)):
            total_sum += nums[right]

            remainder = total_sum % k

            if remainder in prefix:
                count += prefix[remainder]
            prefix[remainder] = prefix.get(remainder, 0) + 1

    
        return count

