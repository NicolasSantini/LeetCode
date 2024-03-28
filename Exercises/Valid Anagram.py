class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettere = {}
        for c in s:
            if c in lettere:
                lettere[c] += 1
            else:
                lettere[c] = 1

        for c in t:
            if c in lettere:
                lettere[c] -= 1
            else:
                return False

        for c in lettere:
            if lettere[c] != 0:
                return False

        return True

    