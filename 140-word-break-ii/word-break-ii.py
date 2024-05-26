class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        for i in range(len(s), -1, -1):
            sentence = []

            for j in range(i, len(s)):
                word = s[i : j + 1]

                if self.solve(word, wordDict):
                    if j == len(s) - 1:
                        sentence.append(word)
                    else:
                        nx = memo.get(j + 1, [])
                        for ch in nx:
                            sentence.append(word + " " + ch)

            memo[i] = sentence

        return memo.get(0, [])

    def solve(self, word: str, word_dict: List[str]) -> bool:
        return word in word_dict