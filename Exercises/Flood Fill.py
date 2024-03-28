#time o(n*m) space o(n*m)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        num = image[sr][sc]

        def fill(sr, sc):
            if sr < 0 or sr >= len(image): return
            if sc < 0 or sc >= len(image[sr]): return
            if image[sr][sc] != num or image[sr][sc] == color: return
            image[sr][sc] = color

            fill(sr - 1, sc)
            fill(sr + 1, sc)
            fill(sr, sc - 1)
            fill(sr, sc + 1)

        fill(sr, sc)
        return image
