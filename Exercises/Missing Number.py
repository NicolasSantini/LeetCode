from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # res = 0
        # for n in nums:
        #     res ^= n
        # for i in range(len(nums)+1):
        #     res ^= i
        # return res

        somma = sum(nums)
        l = len(nums)
        somma_tot = (l * (l + 1)) // 2
        return somma_tot - somma


sol = Solution()
nums = [0, 1]
print(sol.missingNumber(nums))
