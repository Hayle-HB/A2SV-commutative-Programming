import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        i = 0
        n = len(tasks)
        
        while i < n or min_heap:
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]
            
            while i < n and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            process_time, index = heapq.heappop(min_heap)
            time += process_time
            result.append(index)
        
        return result
