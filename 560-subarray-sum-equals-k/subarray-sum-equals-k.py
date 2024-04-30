class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            complement = current_sum - k
            if complement in prefix_sum:
                count += prefix_sum[complement]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count
