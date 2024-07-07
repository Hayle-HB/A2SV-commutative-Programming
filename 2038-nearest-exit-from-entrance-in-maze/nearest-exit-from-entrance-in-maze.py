class Solution:
    def nearestExit(self, maze: List[List[str]], s: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        def is_valid(r, c):
            return 0 <= r < n and 0 <= c < m and maze[r][c] == '.'

        def is_exit(r, c):
            return (r == 0 or r == n - 1 or c == 0 or c == m - 1) and (r != s[0] or c != s[1])

        dxn = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        queue = deque()
        queue.append((s[0], s[1], 0))
        maze[s[0]][s[1]] = '+'

        while queue:
            r, c, step = queue.popleft()

            for dr, dc in dxn:
                nr = r + dr
                nc = c + dc

                if is_valid(nr, nc):
                    if is_exit(nr, nc):
                        return step + 1
                    queue.append((nr, nc, step + 1))
                    maze[nr][nc] = '+'

        return -1
