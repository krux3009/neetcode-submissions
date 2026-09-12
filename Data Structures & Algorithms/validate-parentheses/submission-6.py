class Solution:
    def isValid(self, s):
        open = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for ch in s:
            if ch in open.keys():
                stack.append(ch)
            elif ch in open.values():
                if len(stack) > 0 and open[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0