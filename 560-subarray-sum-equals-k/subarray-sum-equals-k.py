class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        curr = 0

        count = 0

        for num in nums:
            curr += num

            if curr - k in prefix:
                count += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        return count