class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] != mid:
                r = mid - 1
            else:
                l = mid + 1
        return l
        
