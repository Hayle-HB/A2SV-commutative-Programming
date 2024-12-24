class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        words = list(''.join(words))
        
        count = Counter(words)
        for key in count:
            if   count[key] % n != 0:
                return False
        return True
