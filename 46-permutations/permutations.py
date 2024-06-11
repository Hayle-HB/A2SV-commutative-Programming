class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(result, perm):
            nonlocal nums

            if len(perm) == len(nums):
                result.append(perm[:])


            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(result, perm)
                    perm.pop()
        backtrack(result, [])

        return result
        