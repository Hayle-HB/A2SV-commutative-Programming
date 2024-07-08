class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
            n = len(board)
            
            def get_coordinates(square):
                r, c = divmod(square - 1, n)
                if r % 2 == 0:
                    return (n - 1 - r, c)
                else:
                    return (n - 1 - r, n - 1 - c)
            
            visited = set()
            queue = deque([(1, 0)]) 
            
            while queue:
                square, move_count = queue.popleft()
                
                for next_square in range(square + 1, min(square + 6, n * n) + 1):
                    r, c = get_coordinates(next_square)
                    if board[r][c] != -1:
                        next_square = board[r][c]
                    
                    if next_square == n * n:
                        return move_count + 1
                    
                    if next_square not in visited:
                        visited.add(next_square)
                        queue.append((next_square, move_count + 1))
            
            return -1
        