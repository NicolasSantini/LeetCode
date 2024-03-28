from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         p_sum = nums[0]
#         sum = p_sum
#
#         i = 1
#         while i < len(nums):
#             if p_sum <= 0:
#                 p_sum = 0
#             p_sum += nums[i]
#             sum = p_sum if p_sum > sum else sum
#             i+= 1
#
#
#         return sum
#


#interesting DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumMax = current = nums[0]

        for i in range(len(nums) - 1):
            current = max(current + nums[i + 1], nums[i + 1])
            sumMax = max(current, sumMax)

        return sumMax

sol = Solution()
nums = [5, 4, -1, 7, 8]
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [-2, 1]
print(sol.maxSubArray(nums1))
