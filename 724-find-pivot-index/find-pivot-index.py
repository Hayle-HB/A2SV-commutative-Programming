class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        target = sum(nums)

        curr = 0
        for i in range(len(nums)):
            curr += nums[i]

            if curr-nums[i] == target-curr:
                return i
        return -1

            

        
        
        
        