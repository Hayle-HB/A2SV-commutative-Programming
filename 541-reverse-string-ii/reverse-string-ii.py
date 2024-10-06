class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        answer = []
        l = 0
        i = 0
        while l < len(s):
            temp = s[l:l+k]
            if (i % 2 == 0):
                answer.extend(temp[::-1])
            else:
                answer.extend(temp)
            i += 1
            l += k
        return ''.join(answer)
        
            



        
        