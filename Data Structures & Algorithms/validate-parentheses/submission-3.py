class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        M = {'(': ')', '{': '}', '[': ']'}

        for operator in s:
            if operator in M:
                stack.append(operator)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if M[top] != operator:
                    return False
        
        return len(stack) == 0
