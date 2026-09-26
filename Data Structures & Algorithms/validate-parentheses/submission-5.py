class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        
        stack = []
        M = {'(': ')', '{': '}', '[': ']'}

        for elem in s:
            if elem in M:
                stack.append(elem)
            else:
                if len(stack) == 0:
                    return False
                
                top = stack.pop()

                if M[top] != elem:
                    return False
        
        return len(stack) == 0