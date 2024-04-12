from typing import List

#mia soluzione fallimentare
class Solution:
    def trap(self, height: List[int]) -> int:
        def trappolina(height):
            p1, p2 = 0, 1
            size = len(height)
            water = 0
            while p1 < size and p2 < size:
                if height[p1] != 0:
                    while height[p1] > height[p2]:
                        p2 += 1
                        if p2 == size:
                            p1 = p1 + 1
                            p2 = p1 + 1
                            break
                    # ho trovato due punti in cui posso inserire acqua
                    if p2 < size and height[p1] <= height[p2]:
                        water += (p2 - p1 - 1) * min(height[p1], height[p2]) - sum(height[p1 + 1:p2])
                        p1 = p2
                        p2 += 1
                else:
                    p1 += 1
                    p2 += 1
            return water

        return max(trappolina(height), trappolina(height[::-1]))


#soluzione con video
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

sol = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height1 = [4, 2, 3]
height2 = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
print(sol.trap(height1))
