class Solution:
    def sortSentence(self, s: str) -> str:
        Words = s.split(' ')

        Words = sorted(Words, key = lambda x: x[-1])
        Words = " ".join(Words)

        Words = re.sub(r'\d+', '', Words)

        return Words