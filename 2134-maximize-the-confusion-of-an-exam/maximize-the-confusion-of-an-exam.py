class Solution:
    def maxConsecutiveAnswers(self, answer: str, k: int) -> int:
        def confused(char):
            count = 0
            max_conf = 0

            l = 0

            for r in range(len(answer)):
                if answer[r] != char:
                    count +=1
                
                while count > k:
                    if answer[l] != char:
                        count -= 1
                    l += 1
                max_conf = max(max_conf, r - l + 1)
            
            return max_conf
        
        return max(confused('F'), confused('T'))