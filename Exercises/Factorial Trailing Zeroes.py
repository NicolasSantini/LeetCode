class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 5
        res = 0
        while num <= n:
            res += n // num
            num *= 5
        return res