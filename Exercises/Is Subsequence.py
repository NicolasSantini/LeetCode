class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        p1, p2 = 0, 0
        while p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                if p1 == len(s):
                    return True
            p2 += 1

        return False


sol = Solution()
s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))
