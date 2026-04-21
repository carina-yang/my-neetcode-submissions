class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }
        for c in s:
            if c in brackets and len(stack) == 0:
                return False

            if c in brackets and brackets[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0