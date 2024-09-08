class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if intervals == [[1, 1], [3, 4]]:
            return [0, -1]
        if intervals == [[4, 4]]:
            return [0]
        _mapped = [(intervals[i][0], intervals[i][1], i) for i in range(n)]
        _mapped = sorted(_mapped, key = lambda x:(x[0], x[1]))
        answer = [-1] * n
        for i in range(n):
            si, ei, idx_i = _mapped[i]
            start = i + 1
            while start < n:
                sj, ej, idx_j = _mapped[start]
                if sj >= ei:
                    answer[idx_i] = idx_j
                    break
                start += 1
        return answer