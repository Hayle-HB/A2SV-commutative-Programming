class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        curr_sum = 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]


            comp = curr_sum - k

            if comp in prefix:
                count += prefix[comp]
            
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        return count