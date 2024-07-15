from typing import List
from collections import deque

class Solution:
    def __init__(self):
        self.move = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c, visit):  # mark all first islands with first island
            grid[r][c] = 'first island'
            visit.add((r, c))
            for dr, dc in self.move:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visit:
                    if grid[nr][nc] == 1:
                        dfs(nr, nc, visit)

        def find_first():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        return (i, j)
            return None

        def get_first(): # get all the combination of first islands
            queue = deque()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 'first island':
                        queue.append((i, j))
            return queue

        def bfs(queue, visit):  
            step = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for dr, dc in self.move:
                        nr = i + dr
                        nc = j + dc
                        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visit:
                            if grid[nr][nc] == 1:
                                return step + 1
                            visit.add((nr, nc))
                            queue.append((nr, nc))
                step += 1
            return -1  

        r, c = find_first()
        if r is None:
            return -1 

        visited = set()
        dfs(r, c, visited)
        queue = get_first()
        return bfs(queue, visited)-1
