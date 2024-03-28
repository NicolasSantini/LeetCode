#spazio O(1) tempo O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit: int = 0
        minimo: int =prices[0]
        for price in prices:
            if price < minimo:
                #mi salvo il minimo ogni volta
                minimo = price
                #e controllo che la differenza che ho con il minimo sia maggiore di quella precedente
            if price - minimo > profit:
                profit = price - minimo

        return profit
