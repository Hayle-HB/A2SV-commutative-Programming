class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [-1] * (m * n)
        size = [0] * (m * n)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
        
        def index(r, c):
            return r * n + c
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    idx = index(r, c)
                    parent[idx] = idx
                    size[idx] = grid[r][c]
        

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                            union(index(r, c), index(nr, nc))
        
        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    max_fish = max(max_fish, size[find(index(r, c))])
        
        return max_fish
