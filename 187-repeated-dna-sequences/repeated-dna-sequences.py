class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        anser = []

        hash = defaultdict(int)
        for right in range(len(s)-9):
            curr = s[right:right+10]
            hash[curr] += 1
        return [s for s in hash if hash[s] > 1]



        