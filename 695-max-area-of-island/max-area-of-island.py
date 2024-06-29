class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.max_size = 0
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.max_size = max(self.max_size, self.size[rootX])
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.max_size = max(self.max_size, self.size[rootY])
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
                self.rank[rootX] += 1
                self.max_size = max(self.max_size, self.size[rootX])

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            if not grid or not grid[0]:
                return 0

            rows, cols = len(grid), len(grid[0])
            uf = UnionFind(rows * cols)
            directions = [(1, 0), (0, 1)]

            def get_index(r, c):
                return r * cols + c

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                uf.union(get_index(r, c), get_index(nr, nc))

            
            max_area = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        root = uf.find(get_index(r, c))
                        max_area = max(max_area, uf.size[root])

            return max_area