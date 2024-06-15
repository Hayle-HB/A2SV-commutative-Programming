class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap = []
        max_pro = []
        
        for i in range(len(profits)):
            heapq.heappush(min_cap, (capital[i], profits[i]))
        for _ in range(k):
           
            while min_cap and min_cap[0][0] <= w:
                cap, prof = heapq.heappop(min_cap)
                heapq.heappush(max_pro, -prof) 
            
            if not max_pro:
                break
            
            w += -heapq.heappop(max_pro) 
        
        return w