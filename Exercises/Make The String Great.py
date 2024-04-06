class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (s[i] == s[i + 1].upper() and s[i+1].islower()) or (s[i].upper() == s[i + 1] and s[i].islower()):
                s = s[:i] + s[i + 2:]
                i = i - 1 if i != 0 else i
            else:
                i += 1
        return s


sol = Solution()
# s = "leEeetcode"
s = "kkdsFuqUfSDKK"
print(sol.makeGood(s))
