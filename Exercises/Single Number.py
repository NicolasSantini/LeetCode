from typing import List

#non ottima
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         list = []
#         for n in nums:
#             if n in list:
#                 list.remove(n)
#             else:
#                 list.append(n)
#
#         return list[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 0
        for n in nums:
            val = val ^ n
        return val


sol = Solution()
arr = [4,1,2,1,2]
print(sol.singleNumber(arr))