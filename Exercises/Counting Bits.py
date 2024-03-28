class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        pos = 0
        def conta(self,n):
            num = n
            resto = 0
            while num > 0:
                resto += 1 if num % 2 == 1 else 0
                num = int(num/2)

            return resto
        num = 0
        while(num <= n):
            resto = conta(self,num)
            res.append(resto)
            num += 1

        return res