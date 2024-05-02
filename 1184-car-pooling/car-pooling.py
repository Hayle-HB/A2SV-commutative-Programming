class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prifix = [0]*(1002)
        
        
        for n,s,e in trips:
            prifix[e] -= n
            prifix[s] += n
        
        for i in range(1,1002):
            prifix[i] += prifix[i - 1]
        return max(prifix) <= capacity