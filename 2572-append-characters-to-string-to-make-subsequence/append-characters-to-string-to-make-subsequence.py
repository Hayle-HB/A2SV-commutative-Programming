class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        count = len(t)

        idx = 0

        for i in range(len(s)):
            if s[i] == t[idx]:
                idx += 1
                count -= 1
                if count == 0:
                    return 0

        return count
        