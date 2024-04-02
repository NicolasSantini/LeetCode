class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        values = s.split(sep= ' ')
        if len(pattern) != len(values):
            return False
        for i,word in enumerate(values):
            if pattern[i] in dic:
                if word != dic[pattern[i]]:
                    return False
            elif word in dic.values():
                return False
            else:
                dic[pattern[i]] = word


        return True

sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(sol.wordPattern(pattern,s))