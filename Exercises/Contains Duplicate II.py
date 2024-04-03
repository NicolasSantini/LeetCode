from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {} #num -> index
        for i,num in enumerate(nums):
            if num in dic:
                if abs(dic[num] - i) <= k:
                    return True
                else:
                    dic[num] = i
            else:
                dic[num] = i
        return False