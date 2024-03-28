#O(n) entrambi
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for n in set(nums):
            if nums.count(n) > n/2:
                return n
#O(n) di space altro modo
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)

#O(1) space usando due variabili
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #sapendo che il più comune occuperà almeno metà lista posso procedere così:
        max = None
        occ = 0
        for num in nums:
            if occ == 0:
                max = num
            occ = occ + 1 if num == max else occ - 1
        return max