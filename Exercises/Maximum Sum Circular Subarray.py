from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0: return 0
        maxSum,minSum = nums[0], nums[0]
        curMin,curMax = 0,0
        total = 0
        for i in range(size):
            curMin = min(curMin + nums[i],nums[i])
            curMax = max(curMax + nums[i],nums[i])
            total += nums[i]
            if curMax > maxSum:
                maxSum = curMax
            if curMin < minSum:
                minSum = curMin


        return max(maxSum,total-minSum) if maxSum > 0 else maxSum

sol = Solution()
nums = [1,-6,-7,4]
print(sol.maxSubarraySumCircular(nums))