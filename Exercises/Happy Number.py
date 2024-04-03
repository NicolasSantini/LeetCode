class Solution:
    def isHappy(self, n: int) -> bool:
        def f(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num //= 10
            return res
        while n != 4 and n != 1:
            n = f(n)
        return True if n == 1 else False

# #effective solution with set
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         hset = set()
#         while n != 1:
#             if n in hset: return False
#             hset.add(n)
#             n = sum([int(i) ** 2 for i in str(n)])
#         else:
#             return True

sol = Solution()
print(sol.isHappy(19))