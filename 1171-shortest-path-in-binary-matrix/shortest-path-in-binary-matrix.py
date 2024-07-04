class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
                    return -1

        directions = [(-1, -1),  (-1, 0),  (-1, 1),
                      (0,  -1),            (0, 1),
                      (1,  -1),  (1, 0),   (1, 1)]
        
        queue = deque([(0, 0, 1)])
        n = len(grid)
        while queue:
            r, c, dis = queue.popleft()

            if  r == n-1 and c == n-1:
                return dis
            
            for dr, dc in directions:
                nr = r  + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, dis + 1))
                    grid[nr][nc] = 1
            

        return -1
                

        

        
                   
            
