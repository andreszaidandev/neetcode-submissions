class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for par in s:
            if stack and stack[-1] == "(" and par == ")":
                stack.pop()
            elif stack and stack[-1] == "{" and par == "}":
                stack.pop()
            elif stack and stack[-1] == "[" and par == "]":
                stack.pop()
            else:
                stack.append(par)
        return len(stack) == 0
                    