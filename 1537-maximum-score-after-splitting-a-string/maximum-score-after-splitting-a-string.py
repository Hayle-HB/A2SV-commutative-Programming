class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count('1')

        answer = 0
        zero = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero += 1
            elif s[i] == '1':
                one -= 1
            answer = max(answer, zero + one)
        return answer


        