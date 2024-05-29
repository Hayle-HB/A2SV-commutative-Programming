class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target) - 1

        if first < len(nums) and nums[first] == target:
            return [first, end]
        else:
            return [-1, -1]
