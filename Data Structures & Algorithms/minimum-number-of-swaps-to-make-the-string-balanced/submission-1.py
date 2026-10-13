class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == '[':
                stack.append(ch)
            elif len(stack)>0:
                stack.pop()
        return (len(stack)+1)//2