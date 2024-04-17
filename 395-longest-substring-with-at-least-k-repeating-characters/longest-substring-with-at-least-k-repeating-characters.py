class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def is_valid(char_count, k):
            for count in char_count.values():
                if count > 0 and count < k:
                    return False
            return True
        
        max_length = 0
        n = len(s)
        
        for unique_target in range(1, 27):
            char_count = {}
            left = 0
            right = 0
            unique_count = 0
            
            while right < n:
                if unique_count <= unique_target:
                    if right < n:
                        char = s[right]
                        char_count[char] = char_count.get(char, 0) + 1
                        
                        if char_count[char] == 1:
                            unique_count += 1
                        right += 1
                
                if unique_count > unique_target:
                    char = s[left]
                    char_count[char] -= 1
                    if char_count[char] == 0:
                        unique_count -= 1
                    left += 1
                

                if unique_count == unique_target and is_valid(char_count, k):
                    max_length = max(max_length, right - left)
        
        return max_length
