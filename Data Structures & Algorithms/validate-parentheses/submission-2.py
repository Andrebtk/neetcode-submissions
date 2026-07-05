class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        pairs = {'(': ')', '[': ']', '{':'}'}


        for letter in s:
            if letter in pairs:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                
                if letter != pairs[top]:
                    return False
        
        return len(stack) == 0