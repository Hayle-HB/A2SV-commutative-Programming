class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms) 
        Sum = n * (n + 1) // 2 - n
        print(Sum)
        
        queue = deque()
        visit = set()
        queue.append(0)
        visit.add(0)

        while queue:
            curr = queue.popleft()
            visit.add(curr)

            for move in rooms[curr]:
                if move not in visit:
                    queue.append(move)                    
                    
        return sum(visit) == Sum
        
