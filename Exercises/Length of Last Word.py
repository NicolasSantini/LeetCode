class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.strip().split(sep=' ')
        return len(ss[-1])

sol = Solution()
print(sol.lengthOfLastWord("    "))