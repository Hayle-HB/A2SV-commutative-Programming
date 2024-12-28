class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = float('inf')

        curr = 0

        for num in nums:
            curr += num
            _min = min(_min, curr)
        print(_min)
        return 1 if _min >= 1 else abs(_min)+1

       