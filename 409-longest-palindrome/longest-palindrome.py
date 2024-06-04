class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        print(count)
        res = 0
        found = False
        for val in count.values():
            if val >= 2:
                if val % 2 == 0:
                 res += val
                else:
                 res += val - 1
                 found = True
            if val == 1:
                found = True
        
        return res + 1 if found else res