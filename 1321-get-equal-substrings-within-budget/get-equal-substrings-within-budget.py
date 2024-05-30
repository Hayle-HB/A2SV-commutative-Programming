class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def findCost(char1, char2):
            return abs(ord(char1)-ord(char2))
        
        l, r = 0, 0
        n = len(s)
        ans = 0
        while r<n:
            maxCost -= findCost(s[r], t[r])
            while l<=r and maxCost<0:
                maxCost += findCost(s[l], t[l])
                l += 1
            ans = max(ans, (r-l+1))
            r += 1
        return ans

