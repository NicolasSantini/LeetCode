#time O(n) space o(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        sol = 0
        messo = False
        for c in set(s):
            sol += (s.count(c) // 2) * 2
            if (s.count(c) % 2 != 0 and not messo):
                sol += 1
                messo = True
        return sol