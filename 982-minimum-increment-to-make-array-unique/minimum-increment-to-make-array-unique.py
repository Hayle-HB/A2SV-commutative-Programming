class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()  
        moves = 0  # Counter for the number of moves
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:  
                increment = nums[i - 1] - nums[i] + 1
                nums[i] += increment
                moves += increment
        return moves






        