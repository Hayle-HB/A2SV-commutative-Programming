class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word  
        
        word = list(word)
        idx = word.index(ch)
        word[:idx+1] = word[idx::-1]
        
        return ''.join(word)