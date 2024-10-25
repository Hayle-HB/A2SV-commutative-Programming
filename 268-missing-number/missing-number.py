class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Set = set(nums)

        for i in range(len(nums)):
            if i not in Set:
                return i
        return len(nums)