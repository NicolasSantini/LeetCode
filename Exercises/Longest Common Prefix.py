class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = []
        min = 200
        pos = 0
        for j, s in enumerate(strs):
            if len(s) < min:
                min = len(s)
                pos = j

        for c in strs[pos]:
            stack.append(c)
        for s in strs:
            for i, c in enumerate(s):
                if i >= len(stack) or stack[i] != c:
                    stack = stack[:i]
                    break

        return ''.join(stack)