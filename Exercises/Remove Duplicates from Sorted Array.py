from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #remove duplicates in place but keep the order (or shift to the end of the array)
        #return the number of unique elements
        cnt = 0 if len(nums) < 1 else 1
        start, end = 1, len(nums) -1
        while (start <= end):
            #trovo il primo maggiore e lo sposto alla posizione di start
            if nums[start] > nums[start-1]:
                nums[cnt]= nums[start]
                cnt += 1
            start += 1

        return cnt

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)