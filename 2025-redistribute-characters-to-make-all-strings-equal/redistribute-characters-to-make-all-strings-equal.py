class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        word_chr = []
        n = len(words)
        for word in words:
            word_chr.extend(list(word))
        count = Counter(word_chr)
        for key in count:
            if   count[key] % n != 0:
                return False
        return True
