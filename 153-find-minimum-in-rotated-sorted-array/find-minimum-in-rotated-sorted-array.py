class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        Min = nums[0]
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < Min:
                Min = nums[mid]
                high = mid
            else:
                low = mid + 1
        return Min


        