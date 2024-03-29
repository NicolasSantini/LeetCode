from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #remove all occurrencies of val ( or just move them to the end)
        #return the number of elements not equal to val
        start, end = 0, len(nums)-1
        cnt = 0
        while start <= end:
            if nums[start] == val:
                #swap
                nums[end],nums[start] = nums[start],nums[end]
                end -= 1

            else:
                cnt += 1
                start += 1

        return cnt

sol = Solution()
nums = [3,2,2,3]
val = 3.
print(sol.removeElement(nums,val))
print(nums)