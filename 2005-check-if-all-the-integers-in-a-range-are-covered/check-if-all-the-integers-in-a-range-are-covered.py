class Solution:
    def isCovered(self, ranges, left, right):
        for i in range(left, right+1):
            can = False
            for s, e in ranges:
                if  (s <= i and e >= i):
                    can = True
            if not can:
                return False
        return can