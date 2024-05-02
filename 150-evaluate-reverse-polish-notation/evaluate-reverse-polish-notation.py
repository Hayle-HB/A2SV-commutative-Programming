class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def perfome_operation(op1, op2, op):
            if op == '+':
                return op1 + op2
            elif op == '-':
                return op1 - op2
            elif op == '*':
                return op1 * op2
            else:
                return op1  / op2
        stack = []
        op = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                result = perfome_operation(int(op1), int(op2), token) 

                stack.append(result)
                
        return int(stack[0])
        