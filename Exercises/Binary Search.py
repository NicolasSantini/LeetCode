#time complexity O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

    #time complexity O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid
            else:
                right = mid

        return -1