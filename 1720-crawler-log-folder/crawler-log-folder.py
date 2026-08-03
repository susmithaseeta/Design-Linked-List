class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l == '../':
                if len(stack) != 0:
                    stack.pop()
            elif l == './':
                continue
            else:
                stack.append(l)
        return len(stack)
 