class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxGold = 0
        
        def dfs(i, j, cr_gold):
            nonlocal maxGold
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            gold = grid[i][j]
            cr_gold += gold
            maxGold = max(maxGold, cr_gold)
            temp = grid[i][j]
            grid[i][j] = 0
            dfs(i + 1, j, cr_gold)
            dfs(i - 1, j, cr_gold)
            dfs(i, j + 1, cr_gold)
            dfs(i, j - 1, cr_gold)
            grid[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        
        return maxGold