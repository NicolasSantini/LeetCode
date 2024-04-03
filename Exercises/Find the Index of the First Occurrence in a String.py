class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, 0
        len1,len2 = len(haystack),len(needle)
        if len2 >= len1:
            return 0 if haystack == needle else -1
        while p1 < len1:
            while p1 < len1 and (haystack[p1] == needle[p2]):
                p2 += 1
                p1 += 1
                if p2 == len2:
                    return p1 - p2
            p1 = p1 + 1 - p2
            p2 = 0
        return -1

#optimized one for python
# class Solution(object):
#     def strStr(self, haystack, needle):
#         # makes sure we don't iterate through a substring that is shorter than needle
#         for i in range(len(haystack) - len(needle) + 1):
#             # check if any substring of haystack with the same length as needle is equal to needle
#             if haystack[i : i+len(needle)] == needle:
#                 # if yes, we return the first index of that substring
#                 return i
#         # if we exit the loop, return -1
#         return -1
sol = Solution()
print(sol.strStr("mississippi", "issipi"))
