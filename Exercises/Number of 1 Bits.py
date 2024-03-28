# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         def toBinary(num):
#             num = n
#             str = ''
#             while num > 0:
#                 if num % 2 != 0:
#                     str = '1' + str
#                 else:
#                     str = '0' + str
#                 num = num // 2
#
#             return str
#
#         str = toBinary(n)
#
#         return str.count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 != 0: count += 1
            n >>= 1

        return count


sol = Solution()
print(sol.hammingWeight(11))
