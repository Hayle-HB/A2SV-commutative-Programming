class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n+1)}
        rank = [1 for _ in range(1, n+1)]

        def find(x):
            
            while x != parent[x]:
                parent[x] = find(parent[x])
                x = parent[x]
            return x
        
        def union(i, j):
            pi = find(i)
            pj = find(j)

            if pi != pj:
                if rank[pi-1] > rank[pj-1]:
                    parent[pj] = parent[pi]
                elif rank[pj - 1] > rank[pi - 1]:
                    parent[pi] = parent[pj]
                else:
                    parent[pi] = parent[pj]
                    rank[pj - 1] += 1
        ans = 0
        for u, v in edges:
            if find(u) == find(v):
                ans = [u, v]
            else:
                union(u, v)
    

        return ans