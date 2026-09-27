class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        M = {'{': '}', '(': ')', '[': ']'}

        for char in s:
            if char in M:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if M[top] != char:
                    return False
        
        return len(stack) == 0