class Solution:
    def climbStairs(self, n: int) -> int:
        # coppia scalini : numero di modi
        ways = {}

        def steps(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in ways:
                return ways[n]
            else:
                ways[n] = steps(n - 1) + 1
                return ways[n]

        return steps(n)


#versione non ricorsiva con spazio O(1) invece che O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        first,second = 1,2
        for _ in range (3, n-1):
            current = first + second
            first = second
            second = current

        return second