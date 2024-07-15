from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def isPossible(r, c, keys):
            
            if not (0 <= r < n and 0 <= c < m):
                return False
            cell = grid[r][c]
            if cell == '#':
                return False
            if 'A' <= cell <= 'Z' and cell.lower() not in keys:
                return False
            return True
        
        n, m = len(grid), len(grid[0])
        r, c = 0, 0
        keys_needed = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    r, c = i, j
                if 'a' <= grid[i][j] <= 'z':
                    keys_needed += 1
        
        queue = deque([(r, c, "")])
        visited = set((r, c, ""))
        moves = 0
        
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c, keys = queue.popleft()
                
                if len(keys) == keys_needed:
                    return moves
                
                for dr, dc in move:
                    nr, nc = r + dr, c + dc
                    
                    if not isPossible(nr, nc, keys):
                        continue
                    
                    cell = grid[nr][nc]
                    new_keys = keys
                    
                    if 'a' <= cell <= 'z' and cell not in keys:
                        new_keys += cell
                    
                    if (nr, nc, new_keys) not in visited:
                        visited.add((nr, nc, new_keys))
                        queue.append((nr, nc, new_keys))
            
            moves += 1
        
        return -1
