# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         start,end = 0,len(s)-1
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#             start += 1
#             end -= 1
#         return True

# without converting it to a string:
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         num = x
#         s = []
#         while num > 0:
#             s.append(num % 10)
#             num //= 10
#         while x > 0:
#             if s.pop() != x % 10:
#                 return False
#             x //= 10
#
#         return True

# a more efficient solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        new, num = 0, x
        while new < num:
            new = new * 10 + num % 10
            num //= 10

        return new == num or new // 10 == num


sol = Solution()
print(sol.isPalindrome(10))
