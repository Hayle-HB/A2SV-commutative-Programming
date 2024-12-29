class Solution:
    def isCovered(self, ranges, left, right):
        line = [0] * 52

        for s, e in ranges:
            line[s] += 1
            line[e + 1] -= 1
        
        for i in range(1, len(line)):
            line[i] += line[i-1]
        
        return 0 not in line[left:right+1]
