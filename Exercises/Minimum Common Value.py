from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = 0, 0
        if len(nums1) == 0 or len(nums2) == 0:
            return -1
        while nums1[n1] != nums2[n2]:
            if nums1[n1] > nums2[n2]:
                n2 += 1
            else:
                n1 += 1
            if n1 >= len(nums1) or n2 >= len(nums2):
                return -1

        return nums1[n1]
