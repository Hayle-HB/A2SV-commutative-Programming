class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        word_count = [Counter(count) for count in words]

        print(word_count)
        res = []

        for char in word_count[0]:
            min_freq = min(counter[char] for counter in word_count)
            res.extend([char] * min_freq)

        return res
        
        