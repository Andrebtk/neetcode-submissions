class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        

        stack = []
        M = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in M:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()
                if M[top] != c:
                    return False
        
        return len(stack) == 0