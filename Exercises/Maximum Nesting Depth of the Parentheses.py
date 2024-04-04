class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        maxCnt = 0
        for c in s:
            if c == '(':
                cnt += 1
                maxCnt = max(maxCnt, cnt)
            elif c == ')':
                cnt = max(0, cnt - 1)

        return maxCnt

sol = Solution()
s = s = ")"
print(sol.maxDepth(s))