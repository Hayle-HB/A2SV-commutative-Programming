class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        curr = 0

        for idx, num in enumerate(nums):
            curr += num

            if curr - num == total - curr:
                return idx
        return -1
        