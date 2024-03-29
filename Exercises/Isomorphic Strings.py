from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = defaultdict(set)
        map2 = defaultdict(set)

        for i, c in enumerate(s):
            map1[c].add(i)

        for i, c in enumerate(t):
            map2[c].add(i)

        return set(tuple(v) for v in map1.values()) == set(tuple(v) for v in map2.values())

    # soluzione del cristo
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     return [*map(s.index, s)] == [*map(t.index, t)]


sol = Solution()
s = "egg"
t = "add"
print(sol.isIsomorphic(s,t))