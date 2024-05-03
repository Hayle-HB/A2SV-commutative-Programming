class Solution:
    def countElements(self, nums: List[int]) -> int:
        Min = min(nums)
        Max = max(nums)

        if Min == Max:
            return 0
        
        return len(nums) -  nums.count(Min) - nums.count(Max)

        