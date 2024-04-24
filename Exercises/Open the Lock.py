from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if not deadends or not target or '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        visited = set(deadends)
        q = deque()

        q.append(['0000', 0])

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):

                if child not in visited:
                    visited.add(child)
                    q.append([child, turns + 1])

        return -1


sol = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(sol.openLock(deadends, target))
