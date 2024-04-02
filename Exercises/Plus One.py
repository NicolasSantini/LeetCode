from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        if j < 0:
            return [1]
        # se l'ultima cifra è 9 devo portarla a zero
        # e incrementare la cifra precedente (se esiste, altrimenti la creo)
        while j >= 0:
            if digits[j] <= 8:
                digits[j] += 1
                return digits
            else:
                digits[j] = 0
                j -= 1
        return [1] + digits


sol = Solution()
digits = [9, 9, 9, 9]
dig = sol.plusOne(digits)
print(dig)
