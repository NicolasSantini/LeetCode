from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ret = 0
        i = 0
        size = len(tickets)
        while tickets[k] > 0:
            if tickets[i] > 0:
                tickets[i] -= 1
                ret += 1
            i += 1
            if i == size:
                i = 0
        return ret


sol = Solution()
tickets = [5,1,1,1]
k = 0
print(sol.timeRequiredToBuy(tickets, k))
