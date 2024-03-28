#o(n)) time and o(1) mem
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #con indici negativi posso scorrere l'array al contrario
        aLen, bLen = -len(a), -len(b)
        i,carry,res = -1,0, ""

        while i >= aLen or i >= bLen:
            aBit = int(a[i]) if i >= aLen else 0
            bBit = int(b[i]) if i >= bLen else 0

            val = aBit + bBit + carry
            res = str(val%2) + res
            carry = val // 2

            i -= 1

        return str(carry) + res if carry  else res