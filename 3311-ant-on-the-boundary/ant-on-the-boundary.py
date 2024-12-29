class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0

        curr = 0

        for num in nums:
            curr += num

            if curr == 0:
                count += 1
        return count
        