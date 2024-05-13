from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        ans = rows * (1 << (cols - 1))  
        
        for j in range(1, cols):
            col_count = sum(grid[i][j] == grid[i][0] for i in range(rows))
            ans += max(col_count, rows - col_count) * (1 << (cols - 1 - j))
        
        return ans
