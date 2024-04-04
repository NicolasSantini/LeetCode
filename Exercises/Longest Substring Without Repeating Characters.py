class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 0
        dim = len(s)
        charSet = set()
        maxSize = 0

        for p2 in range(dim):
            while s[p2] in charSet:
                charSet.remove(s[p1])
                p1 += 1
            charSet.add(s[p2])
            maxSize = max(maxSize,p2 - p1 + 1)
        return maxSize


sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))
