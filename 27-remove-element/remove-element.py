class Solution(object):
    def removeElement(self, nums, val):
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left
        