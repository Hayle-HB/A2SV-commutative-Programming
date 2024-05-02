class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zeros_left = 0
        ones_right = s.count('1')
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
            
            score = zeros_left + ones_right
            max_score = max(max_score, score)
        
        return max_score
