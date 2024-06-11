class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to handle duplicates
        nums.sort()
        result = []

        def backtrack(perm, used):
            if len(perm) == len(nums):
                result.append(perm[:])  # Add a copy of the permutation to result
                return

            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                used[i] = True 
                perm.append(nums[i]) 
                backtrack(perm, used)  
                perm.pop()  
                used[i] = False  

        backtrack([], [False] * len(nums))
        return result
