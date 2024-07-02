class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [False] * n

        for u, v in edges:
            incoming[v]  = True
        
        return [i for i in range(n) if incoming[i] == False]