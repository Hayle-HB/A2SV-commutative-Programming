class UF:
    def __init__(self,n):
        self.par=[i for i in range(n+1)]
        self.n=n
    def find(self,x):
        while x!=self.par[x]:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x
    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py: return 0
        self.par[py], self.n = px, self.n-1
        return 1
    def connected(self,): return self.n==1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a,b=UF(n),UF(n)
        count=0
        edges.sort(key=lambda x:x[0], reverse=True)
        for t,x,y in edges:
            if t==3: count+= a.union(x,y) | b.union(x,y)
            elif t==1: count+= a.union(x,y)
            elif t==2: count+= b.union(x,y)
            if a.connected() and b.connected(): return len(edges)-count
        return -1 