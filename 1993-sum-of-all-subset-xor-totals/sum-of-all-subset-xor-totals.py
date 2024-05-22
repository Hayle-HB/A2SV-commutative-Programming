class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res |= num
        xor =  res * (1 << (len(nums) - 1))

        return xor