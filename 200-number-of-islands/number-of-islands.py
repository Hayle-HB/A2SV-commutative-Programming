class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        n = len(grid)
        m = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < n  and 0 <= c < m and grid[r][c] == '1'):
                return
            grid[r][c] = '0'
            for dr, dc in direction:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
    
        return count

