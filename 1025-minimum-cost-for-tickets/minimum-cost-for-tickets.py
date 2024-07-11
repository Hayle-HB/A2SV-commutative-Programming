class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        day_set = set(days)
        max_day = days[-1]
        def dp(day):
            if day > max_day:
                return 0
            if day in memo:
                return memo[day]
            
            if day not in day_set:
                memo[day] = dp(day + 1)
                return memo[day]
            
            costs1 = dp(day  + 1) + costs[0]
            costs2 = dp(day + 7) + costs[1]
            costs3 = dp(day + 30) + costs[2]

            _min = min(costs1, costs2, costs3)
            memo[day] = _min
            return memo[day]
        return dp(days[0])