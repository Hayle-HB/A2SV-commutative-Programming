class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []

        l = 0

        while l < len(s):
            word = ''
            while l < len(s) and  s[l] != ' ':
                word += s[l]
                l += 1
            answer.append(word[::-1])
            while l < len(s) and  s[l] == ' ':
                answer.append(' ')
                l += 1
        return ''.join(answer)