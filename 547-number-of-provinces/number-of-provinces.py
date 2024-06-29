class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.parent = [ i for i in range(n)]
        self.rank = [1] * n

        def find(i):
            if self.parent[i] == i:
                return i
            else:
                self.parent[i] = find(self.parent[i])
                return self.parent[i]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)

            if pi != pj:
                if self.rank[pi] > self.rank[pj]:
                    self.parent[pj] = pi
                elif self.rank[pj] > self.rank[pi]:
                    self.parent[pi] = pj
                else:
                    self.parent[pi] = pj
                    self.rank[pj] += 1
        
        for i in range((n)):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)
                    
        unique_roots = set(find(i) for i in range(n))
        return len(unique_roots)

                    
            
            
        

        