class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        size = len(s)
        cnt = 0  #counting the opening parenthesis
        pos = []
        i = 0
        while i < size:
            if s[i] == '(':
                cnt += 1
                pos.append(i)
            elif s[i] == ')':
                if cnt != 0:
                    cnt -= 1
                    pos.pop()
                else:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                    size -= 1
            i += 1
        if pos:
            for p in pos[::-1]:
                s = s[:p] + s[p + 1:]

        return s

sol = Solution()
s = "))(("
print(sol.minRemoveToMakeValid(s))