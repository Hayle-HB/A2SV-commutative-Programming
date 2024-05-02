class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1

        while left < right:
            Sum = nums[left] + nums[right]

            if Sum == 0:
                return nums[right]
            elif Sum < 0:
                left += 1
            else:
                right -= 1
        
        return -1
        