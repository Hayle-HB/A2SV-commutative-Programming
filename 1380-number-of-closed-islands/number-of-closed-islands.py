from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])
        
        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = 1 
            
            while stack:
                r, c = stack.pop()
                
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        grid[nr][nc] = 1  
                        stack.append((nr, nc))
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i == 0 or i == n-1 or j == 0 or j == m-1):
                    dfs(i, j)
        

        closed_islands = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    closed_islands += 1
        
        return closed_islands
