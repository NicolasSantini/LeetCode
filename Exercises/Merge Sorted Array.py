from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[:] = nums1[:m]
#         nums2[:] = nums2[:n]
#         i,j = 0,0
#         while j < n:
#             if i >= m+j or nums2[j] <= nums1[i]: #inseriamo
#                 nums1[:] = nums1[:i] + nums2[j:j+1] + nums1[i:]
#                 j += 1
#             i += 1
#
#         print(nums1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if nums1[m-1] >= nums2[n-1] and m>0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [1,0]
# m = 1
# nums2 = [2]
# n = 1

sol.merge(nums1,m,nums2,n)
print(nums1)