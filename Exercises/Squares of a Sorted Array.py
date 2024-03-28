import math
#O(n) time and space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for num in nums:
            squares.append(int(math.sqrt(num)))

        return sorted(squares)

#soluzione senza il sorted con two pointers
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_pointer, right_pointer = 0, len(nums)-1
        curr = right_pointer
        final = [0] * len(nums)

        left_square = nums[left_pointer] ** 2
        right_square = nums[right_pointer] ** 2


        while curr >= 0:
            if left_square > right_square:
                final[curr] = left_square
                left_pointer += 1
                left_square = nums[left_pointer] ** 2

            else:
                final[curr] = right_square
                right_pointer -= 1
                right_square = nums[right_pointer] ** 2

            curr -= 1

        return final