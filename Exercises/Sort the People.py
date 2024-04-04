from typing import List


# molto poco ottimizzata ma prima soluzione pensata
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         for i in range(len(names) - 1):
#             idx = heights.index(max(heights[i:]))
#             names[i], names[idx] = names[idx], names[i]
#             heights[i], heights[idx] = heights[idx], heights[i]
#
#         return names

# soluzione ottenuta guardando altri utenti
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_dict = dict(zip(heights, names))
        names.clear()
        for key in sorted(h_dict.keys(),reverse=True):
            names.append(h_dict[key])
        return names