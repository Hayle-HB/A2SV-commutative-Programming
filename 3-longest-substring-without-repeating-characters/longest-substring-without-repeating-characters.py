class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        left = 0
        charIndex = {}  
        
        for right in range(n):
            currentChar = s[right]
            
            if currentChar in charIndex and charIndex[currentChar] >= left:
                left = max(left, charIndex[currentChar] + 1)
            
            charIndex[currentChar] = right
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
