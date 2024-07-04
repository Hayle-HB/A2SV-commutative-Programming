class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        left = 0
        ans = set()
        while left < len(nums):
            curr = nums[left]
            
            if curr != nums[curr - 1]:
                nums[left], nums[curr - 1] = nums[curr - 1], nums[left]
            else:
                if left != curr - 1 and curr not in ans:
                    ans.add(curr)
                
                left += 1
        
        return list(ans)