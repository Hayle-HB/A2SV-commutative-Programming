class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
            start = "".join(str(num) for row in board for num in row)
            goal = "123450"
            
           
            moves = {
                0: [1, 3],
                1: [0, 2, 4],
                2: [1, 5],
                3: [0, 4],
                4: [1, 3, 5],
                5: [2, 4]
            }
            
            def get_neighbors(state):
                zero_index = state.index('0')
                neighbors = []
                for move in moves[zero_index]:
                    new_state = list(state)
                    new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
                    neighbors.append("".join(new_state))
                return neighbors
            
            queue = deque([(start, 0)]) 
            visited = set([start])
            
            while queue:
                current_state, moves_count = queue.popleft()
                if current_state == goal:
                    return moves_count
                for neighbor in get_neighbors(current_state):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, moves_count + 1))
            
            return -1 
