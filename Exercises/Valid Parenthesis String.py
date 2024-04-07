class Solution:
    def checkValidString(self, s: str) -> bool:
        min_a, max_a = 0,0
        for c in s:
            if c == '(':
                min_a += 1
                max_a += 1
            elif c == ')':
                min_a -= 1
                max_a -= 1
            else:
                min_a -= 1
                max_a += 1
            min_a = max(min_a,0)
            if max_a < 0: return False

        return True if min_a == 0 else False

sol = Solution()
s = "()"
print(sol.checkValidString(s))
