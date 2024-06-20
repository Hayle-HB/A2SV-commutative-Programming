class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def canRepair(mid):
            total = 0

            for rank in ranks:
                total += int(math.sqrt(mid / rank))

                if total >= cars:
                    return True
            return False


        
        lower = 1
        upper = max(ranks) * cars * cars

        while lower < upper:
            mid = (lower + upper) // 2
            if canRepair(mid):
                upper = mid
            else:
                lower = mid + 1
        
        return lower