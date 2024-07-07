class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])


        parent = {i*m + j: i * m + j for i in range(n) for j in range(m)}
        rank = [1] * (n * m)


        def find(i):
            if parent[i] == i:
                return parent[i]
            else:
                parent[i] = find(parent[i])
            
            return parent[i]

        def union(i, j):
            pi = find(i)
            pj = find(j)

            if rank[pi] > rank[pj]:
                parent[pj] = pi
            elif rank[pj] > rank[pi]:
                parent[pi] =pj
            else:
                parent[pj] = pi
                rank[pi] += 1

        dxn = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]


        for i in range(n):
            for j in range(m):

                if grid[i][j] == '1':

                    for dr, dc in dxn:
                        nr = i  + dr
                        nc = j  + dc
                    
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '1':
                            union(i * m + j, nr * m + nc)
        
        answer = set()


        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    item = find(i*m + j)
                    answer.add(item)
        
        return len(answer)

