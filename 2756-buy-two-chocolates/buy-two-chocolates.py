class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        Min1, Min2 = max(prices), max(prices)

        for num in prices:
            if num < Min1:
                Min2 = Min1
                Min1 = num
            elif num < Min2 and num >= Min1:
                Min2 = num
        print(Min1 , Min2)
        return money if money-(Min1 + Min2) < 0 else money-(Min1 + Min2)
        