class Solution:
    def isCovered(self, ranges, left, right):
        line = [0] * 52

        for s, e in ranges:
            line[s] += 1
            line[e + 1] -= 1
        curr = 0
        for i in range(1, right+1):
            curr += line[i]

            if i >= left and curr == 0:
                return False
        return True
