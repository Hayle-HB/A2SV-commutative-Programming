class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()

        idx = 0

        for i in range(len(nums)):

            idx  = nums[i]-1

            while idx != i:
                if nums[idx] == idx + 1:
                    ans.add(idx + 1)
                    break
                nums[idx], nums[i] = nums[i], nums[idx]
                idx = nums[i] - 1
        return list(ans)
                
            


        