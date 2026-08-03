class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '{[(':
                stack.append(c)
            elif len(stack)==0 or (
                c==')' and stack.pop()!='(' or
                c==']' and stack.pop()!='[' or
                c=='}' and stack.pop()!='{'
            ):
                return False
        return True if len(stack)==0 else False
