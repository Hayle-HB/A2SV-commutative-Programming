class Solution:
    def maxPower(self, s: str) -> int:
        count, curr = 0, 0

        for idx in range(1, len(s)):
            if s[idx] == s[idx-1]:
                curr += 1
            else:
                count = max(count, curr)
                curr = 0
        count = max(count, curr)
        return count + 1
        