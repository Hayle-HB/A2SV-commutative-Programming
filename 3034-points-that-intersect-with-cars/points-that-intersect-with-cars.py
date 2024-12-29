class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        line = [0] * (102)

        for s, e in nums:
            line[s] += 1
            line[e+1] -= 1
        
        for i in range(1, len(line)):
            line[i] += line[i-1]
        
        return sum(1 for i in line if i != 0)
        