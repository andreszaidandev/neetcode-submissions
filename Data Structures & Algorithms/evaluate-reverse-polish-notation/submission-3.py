class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tokens[i] == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            elif tokens[i] == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
