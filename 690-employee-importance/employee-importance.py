"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {emp.id: emp for emp in employees}

        total = 0
        queue = deque()
        queue.append(id)
        while queue:
            curr = queue.popleft()
            total += graph[curr].importance

            for sub in graph[curr].subordinates:
                    queue.append(sub)
        
        return total

            

        
        