class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))  
        n = len(scores)
        dp = [0] * n  
        
        for i in range(n):
            dp[i] = players[i][1] 
            for j in range(i):
                if players[i][1] >= players[j][1]:  
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        
        return max(dp)
