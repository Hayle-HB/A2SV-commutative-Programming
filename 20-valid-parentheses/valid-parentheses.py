class Solution(object):
    def isValid(self, s):
        stack = []
        # Use dictionaries to map open and close brackets
        open_to_close = {'(': ')', '{': '}', '[': ']'}
        
        for ch in s:
            # If the character is an opening bracket, push to stack
            if ch in open_to_close:
                stack.append(ch)
            else:
                # If it's a closing bracket, check the stack
                if not stack:
                    return False
                else:
                    # Pop the top of the stack and check if it matches the closing bracket
                    p = stack.pop()
                    if open_to_close[p] != ch:
                        return False
        
        # If the stack is empty at the end, the parentheses are balanced
        return len(stack) == 0
