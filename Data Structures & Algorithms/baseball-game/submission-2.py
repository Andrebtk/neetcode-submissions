class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []


        sumScore = 0


        for op in operations:
            if op == '+':
                x = stack[-1]
                y = stack[-2]
                stack.append(x + y)
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        for elem in stack:
            sumScore += elem
        return sumScore