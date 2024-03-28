#space O(n) time O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringa = s.strip()
        list1 = [c.lower() for c in s if c.isalnum()]
        list2 = list1[::-1]
        return True if list1 == list2 else False

