class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(capacity):
            total = 0
            days_needed = 1
            for weight in weights:
                total += weight
                if total > capacity:
                    days_needed += 1
                    total = weight
                    if days_needed > days:
                        return False
            return True
        lower = max(weights)
        upper  = sum(weights)

        answer = 0
        while lower <= upper:
            mid = (lower + upper) // 2

            if possible(mid):
                upper  = mid - 1
            else:
                lower = mid + 1
        
        return lower

        