class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mappa = {}
        for c in magazine:
            if c in ransomNote:
                mappa[c] += 1
            else:
                mappa[c] = 1
        for c in ransomNote:
            if c in mappa and mappa[c] > 0:
                mappa[c] -= 1
            else:
                return False
        return True
