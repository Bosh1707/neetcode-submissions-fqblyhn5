class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack or (stack[-1] == '[' and char != ']') or \
                (stack[-1] == '{' and char != '}') or \
                (stack[-1] == '(' and char != ')'):
                    return False
                stack.pop()
        return not stack