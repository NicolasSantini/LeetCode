from collections import deque
from typing import List

#soluzione disastosa mia dopo tips
# class Solution:
#     def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
#         if not deck:
#             return deck
#         deck = sorted(deck)
#         size = len(deck)
#         final = [0] * (size)
#         indexes = deque(range(0, size))
#
#         while indexes:
#             final[indexes[0]] = deck[0]
#             deck.pop(0)
#             indexes.popleft()
#             if indexes:
#                 indexes.append(indexes.popleft())
#
#         return final

#soluzione ottimale
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        q = deque(range(len(deck)))

        for n in deck:
            i = q.popleft()
            res[i] = n
            if q:
                q.append(q.popleft())

        return res

sol = Solution()
deck = [17, 13, 11, 2, 3, 5, 7]
print(sol.deckRevealedIncreasing(deck))
