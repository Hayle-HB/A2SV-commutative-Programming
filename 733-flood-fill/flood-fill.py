class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        queue = deque()
        start = image[sr][sc]
        visit = set()
        queue.append((sr, sc))
        n, m = len(image), len(image[0])
        while queue:
            r, c = queue.popleft()
            visit.add((r, c))
            image[r][c] = color

            for dr, dc in direction:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n:
                    if 0 <= nc < m:
                        if image[nr][nc] == start:
                            if (nr, nc) not in visit:
                                queue.append((nr, nc))
        return image