class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracker(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                backtracker(i + 1, path + [nums[i]])

        result = []
        backtracker(0, [])
        return result