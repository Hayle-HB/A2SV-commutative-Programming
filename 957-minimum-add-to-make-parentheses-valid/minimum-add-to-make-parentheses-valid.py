class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(1)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
        
        return count + len(stack)
        

        