class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def how(mid):
            hour = 0

            for pile in piles:
                 hour += (pile + mid - 1) // mid
            return hour <= h

        
        Min = 1
        Max = max(piles)

        while Min < Max:
            mid = (Min + Max) // 2

            if how(mid):
                Max = mid
            else:
                Min = mid + 1
        
        return Min
