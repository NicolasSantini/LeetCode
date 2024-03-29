from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            med = (start + end) // 2
            if target > nums[med]:
                start = med + 1
            elif target < nums[med]:
                end = med - 1
            else:
                return med

        return start


sol = Solution()
nums = [1,3]
target = 2
print(sol.searchInsert(nums, target))
