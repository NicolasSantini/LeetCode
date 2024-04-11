class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        counter = 0
        n = len(num)

        if n == k: return "0"

        for i in range(n):
            while k and res and res[-1] > num[i]:
                res.pop()
                k -= 1
            res.append(num[i])

        while k:
            res.pop()
            k -= 1

        return "".join(res).lstrip('0') or "0"

        # ret = ''
        # i = 0
        # size = len(num)
        # while i < size-1:
        #     if k == 0:
        #         ret += num[i:]
        #         break
        #     if num[i] <= num[i + 1]:
        #         ret += num[i]
        #     else:
        #         k -= 1
        #     i += 1
        # if i == size-1:
        #     ret += num[i]
        # if k != 0:
        #     ret = ret[:-k]
        # ret = int(ret) if ret else 0
        # return str(ret)


sol = Solution()
num = "12340"
k = 3
print(sol.removeKdigits(num, k))
