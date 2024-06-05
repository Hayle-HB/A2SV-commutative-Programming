class Solution:
    def breakPalindrome(self, word: str) -> str:
        if len(word) <= 1:
            return ""
        
        word = list(word)
        for i in range(len(word) // 2):
            if word[i] != 'a':
                word[i] = 'a'
                return ''.join(word)
        
        word[-1] = 'b'
        return ''.join(word)
