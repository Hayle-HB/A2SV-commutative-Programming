class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, result = len(grid), []

        for i in range(1, n - 1):
            new_row = []
            for j in range(1, n - 1):
                temp = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        temp = max(temp, grid[k][l])

                new_row.append(temp)
            result.append(new_row)

        return result