class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for elem in tokens:
            if elem == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                val = val1 + val2
                stack.append(val)
            elif elem == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2 - val1
                stack.append(val)
            elif elem == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                val = val1 * val2
                stack.append(val)
            elif elem == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                val = int(val2 / val1)
                stack.append(val)
            else:
                stack.append(int(elem))

        return stack[0]