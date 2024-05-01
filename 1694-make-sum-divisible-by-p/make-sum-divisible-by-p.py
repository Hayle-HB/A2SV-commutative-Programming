class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        if total_sum % p == 0:
            return 0
        
        rem = total_sum % p
        prefix_sum = 0
        prefix_sum_indices = {0: -1}
        minlen = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target_rem = (prefix_sum - rem) % p
            if target_rem in prefix_sum_indices:
                minlen = min(minlen, i - prefix_sum_indices[target_rem])
            prefix_sum_indices[prefix_sum] = i

        return minlen if minlen < len(nums) else -1
