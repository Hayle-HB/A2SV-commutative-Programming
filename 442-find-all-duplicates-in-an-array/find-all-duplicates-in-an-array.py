class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        left = 0
        
        while left < len(nums):
            curr = nums[left]
            
            if curr != nums[curr - 1]:
                nums[left], nums[curr - 1] = nums[curr - 1], nums[left]
            else:
                if left != curr - 1:
                    ans.append(curr)
                left += 1
        
        return list(set(ans))