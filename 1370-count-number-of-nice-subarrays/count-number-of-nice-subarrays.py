class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = {0:1}
        Sum = 0

        
        for num in nums:
            Sum += num % 2

            if Sum - k in prefix:
                count += prefix[Sum-k]
            
            if Sum in prefix:
                prefix[Sum] += 1
            else:
                prefix[Sum] = 1
        
        return count
