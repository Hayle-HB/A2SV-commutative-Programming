class Solution:
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        for  idx in range(left, len(nums)):
            nums[idx] = 0

     