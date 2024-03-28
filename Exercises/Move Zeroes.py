class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in realtà mi sa che basta usare lo stack
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] == 0:
                nums.append(0)
                nums.remove(0)
                end -= 1
            start += 1


#posso metterci meno passaggi se metto un puntatore all'inizio e uno su ogni zero che trovo.
#ogni volta che trovo un valore successivo a uno zero lo sposto al posto dello zero, così facendo
#tutti gli zeri si sposteranno alla fine
#o(n) tempo o(1) spazio
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0 and first_zero == -1:
                first_zero = i
            elif nums[i] != 0 and first_zero != -1:
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1

