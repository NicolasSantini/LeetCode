from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        size = len(intervals) - 1
        i = 0
        intervals.sort(key=lambda x: x[0])
        while i < size:
            if intervals[i][1] >= intervals[i + 1][0]:  # allora li devo unire
                if intervals[i][1] < intervals[i + 1][1]:
                    intervals[i][1] = intervals[i + 1][1]
                intervals.remove(intervals[i+1])
                size -= 1
            else:
                i += 1

        return intervals

sol = Solution()
intervals = [[1,4],[0,0]]
print(sol.merge(intervals))