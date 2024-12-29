class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

           stack = []
           push = 0
           pop = 0
           while push < len(pushed):
                stack.append(pushed[push])
                push += 1

                while stack and stack[-1] == popped[pop]:
                    stack.pop()
                    pop += 1
           return len(stack) == 0
                
                










