class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [-1, 0, 1, 0, -1]
        rows, cols = len(grid), len(grid[0])
        visit = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visit[i][j] = 1
        distance = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                grid[x][y] = distance
                for k in range(4):
                    r, c = x + directions[k], y + directions[k + 1]
                    if r < 0 or r == rows or c < 0 or c == cols or visit[r][c] == 1:
                        continue
                    visit[r][c] = 1
                    queue.append((r, c))
            distance += 1

        res = float("inf")
        max_heap = [(-grid[0][0], 0, 0)]
        heapq.heapify(max_heap)
        visit[0][0] = 2
        while max_heap:
            cur, x, y = heapq.heappop(max_heap)
            res = min(res, -cur)
            if x == rows - 1 and y == cols - 1:
                return res
            for k in range(4):
                r, c = x + directions[k], y + directions[k + 1]
                if r < 0 or r == rows or c < 0 or c == cols or visit[r][c] == 2:
                    continue
                visit[r][c] = 2
                heapq.heappush(max_heap, (-grid[r][c], r, c))
        return -1