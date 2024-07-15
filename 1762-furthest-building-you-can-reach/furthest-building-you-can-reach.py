import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        max_heap = []
        
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(max_heap, diff)
                if len(max_heap) > ladders:
                    bricks -= heapq.heappop(max_heap)
                if bricks < 0:
                    return i
        
        return n - 1
