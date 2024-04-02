# class Solution:
#     def mySqrt(self, x: int) -> int:
#         less = 1
#         more = 2
#         if x == 0: return 0
#         while 1:
#             if less * less <= x < more * more:
#                 return less
#             else:
#                 less += 1
#                 more += 1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        first, last = 1, x
        while first <= last:
            mid = (first + last ) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid -1
            else:
                first = mid + 1
        return last

sol = Solution()
print(sol.mySqrt(10))
