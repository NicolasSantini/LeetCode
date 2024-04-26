from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        dictionary.sort()
        dictionary.sort(key=len, reverse=True)

        for word in dictionary:
            if len(word) > len(s):
                continue
            cnt = 0
            i = 0
            for letter in word:
                if letter not in s:
                    continue
                else:
                    while i < len(s):
                        if s[i] == letter:
                            cnt += 1
                            i += 1
                            break
                        i += 1
            if cnt == len(word):
                return word

        return ''


sol = Solution()
s = "abce"
dictionary = ["abe","abc"]
print(sol.findLongestWord(s,dictionary))