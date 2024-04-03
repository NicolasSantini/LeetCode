from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2 = 0, 0
        dim = len(nums)
        min_sub = dim
        ctrl = False
        if dim == 0:
            return 0
        curr_sum = 0

        while p2 < dim:
            curr_sum += nums[p2]
            p2 += 1

            while curr_sum >= target and p1 < p2:
                if p2 - p1 <= min_sub:
                    ctrl = True
                    min_sub = p2 - p1

                curr_sum -= nums[p1]
                p1 += 1

        return min_sub if ctrl else 0


sol = Solution()
target = 16
nums = [10,2,3]
print(sol.minSubArrayLen(target, nums))
