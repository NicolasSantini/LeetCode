#tempo o(n^2) e memoria 0(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#tempo o(n) memoria o(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_elem = {}
        for i,num in enumerate(nums):
            diff = target - nums[i]
            if diff in prev_elem:
                return [prev_elem[diff], i]
            prev_elem[num] = i
        return
