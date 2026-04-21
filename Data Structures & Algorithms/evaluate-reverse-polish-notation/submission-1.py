class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b, 
            '*': lambda a, b: a * b,
            '/': lambda a, b: math.trunc(a / b)}
        for token in tokens:
            if token in operators:

                num2 = stack.pop()
                num1 = stack.pop()
                val = operators[token](num1, num2)
                stack.append(val)
            else:
                stack.append(int(token))
        
        return stack[-1]
