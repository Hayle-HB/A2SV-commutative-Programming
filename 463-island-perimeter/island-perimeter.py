class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        square_water = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:

                    if row == 0 or grid[row - 1][col] == 0:
                        square_water += 1

                    if row == len(grid) - 1 or grid[row + 1][col] == 0:
                        square_water += 1

                    if col == 0 or grid[row][col - 1] == 0:
                        square_water += 1

                    if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                        square_water += 1
        
        return square_water
