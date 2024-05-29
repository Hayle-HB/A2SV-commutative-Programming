class Solution:
    def decodeString(self, s: str) -> str:
        # we can use stack for this question implementaion but 
        #since our topic is recurrsion, lets solve with recurrsion
        def helper(s, i):
            ans = ""
            n = 0
            while i < len(s):
                if s[i].isdigit():
                    n = n * 10 + int(s[i])
                elif s[i] == '[':
                    ext, i = helper(s, i + 1)
                    ans += n * ext 
                    n = 0  
                elif s[i] == ']':
                    return ans, i
                else:
                    ans += s[i]
                i += 1
            return ans, i 
        
        return helper(s, 0)[0]
