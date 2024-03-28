# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return True

#O(log n) tempo e spazio O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            med = (start + end) // 2
            if isBadVersion(med):
                end = med
            else:
                start = med + 1
        return start
