from collections import defaultdict
from typing import List


# union-find algo --> not really understood
# class Union:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#
#     def union(self, i, j):
#         parI = self.find(i)
#         parJ = self.find(j)
#         self.parent[parI] = parJ
#
#     def find(self, i):
#         tempI = i
#         while self.parent[tempI] != tempI:
#             tempI = self.parent[tempI]
#         self.parent[i] = tempI
#         return tempI
#
#
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         uf = Union(n)
#
#         for s, d in edges:
#             uf.union(s, d)
#
#         return uf.find(source) == uf.find(destination)


# dfs algo
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:  # adding both neighbours to the dict
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def find(node, visited):
            if node == destination:
                return True
            if node not in visited:
                visited.add(source)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if find(neighbor, visited):
                        return True
            return False

        return find(source, visited)


sol = Solution()
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print(sol.validPath(3, edges, source, destination))
