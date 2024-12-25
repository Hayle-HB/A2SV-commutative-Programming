class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash = set(list(allowed))
        count = 0
        for word in words:
            all = True
            for ch in list(word):
                if ch not in hash:
                    all = False
            if all:
                count += 1
        return count