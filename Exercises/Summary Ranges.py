from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # se i valori sono consecutivi ritorno 'a -> b' altrimenti solo 'a'
        if len(nums) == 0:
            return []
        buf = [nums[0]]
        final = []
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                buf.append(nums[i])
            else:
                final.append(str(buf[0]) if len(buf) == 1 else str(buf[0]) + '->' + str(buf[len(buf) - 1]))
                buf = [nums[i]]
        final.append(str(buf[0]) if len(buf) == 1 else str(buf[0]) + '->' + str(buf[len(buf) - 1]))
        return final


sol = Solution()
nums = [0, 1, 2, 4, 5, 7]
print(sol.summaryRanges(nums))
