#o(n) doppia
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numeri = {}
        for num in nums:
            if num in numeri:
                return True
            else:
                numeri[num] = True

        return False