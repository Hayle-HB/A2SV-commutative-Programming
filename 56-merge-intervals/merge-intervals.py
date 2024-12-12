class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0])

        ans = []


        left = 0

        while left < len(intervals):
            start, end = intervals[left]
           
            while left < len(intervals)-1 and  intervals[left+1][0] <= end:
                left += 1
                end = max(end, intervals[left][1])
            ans.append([start, end])
            left += 1
        return ans
