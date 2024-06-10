class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
            n = len(grid)
            
            max_in_row = [max(row) for row in grid]
            max_in_col = [max(grid[i][j] for i in range(n)) for j in range(n)]
            
            total = 0
            for i in range(n):
                for j in range(n):
                    height = min(max_in_row[i], max_in_col[j])
                    if height > grid[i][j]:
                        total += height - grid[i][j]
            
            return total