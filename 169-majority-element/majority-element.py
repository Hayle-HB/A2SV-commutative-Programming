class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        n = len(nums)

        for c in count:
            if count[c] > n // 2:
                return c
        