class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[-i - 1] = right[-i] + nums[-i]
        for i, num in enumerate(nums):
            if num != 0: continue
            if left[i] == right[i]: res += 2
            if abs(left[i] - right[i]) == 1: res += 1
        return res