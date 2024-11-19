class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        one, two = 0, 0
        merge = []

        while one < len(word1) and two < len(word2):
            s1, s2 = word1[one], word2[two]

            if s1 > s2:
                merge.append(s1)
                one += 1
            elif s2 > s1:
                merge.append(s2)
                two += 1
            else:
                if word1[one:] > word2[two:]:
                    merge.append(s1)
                    one += 1
                else:
                    merge.append(s2)
                    two += 1
        
        merge.append(word1[one:])
        merge.append(word2[two:])

        return ''.join(merge)
        