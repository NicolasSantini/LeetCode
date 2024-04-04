from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        sum1, sum2 = 0, 0
        cnt = 0
        for val1 in player1:
            sum1 += val1 if cnt < 1 else val1 * 2
            cnt = cnt - 1 if val1 != 10 else 2
        cnt = 0
        for val2 in player2:
            sum2 += val2 if cnt < 1 else val2 * 2
            cnt = cnt - 1 if val2 != 10 else 2

        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return 2
        else:
            return 0
       