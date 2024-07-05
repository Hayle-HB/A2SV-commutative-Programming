class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        max_len = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                temp = len(adj[i]) + len(adj[j])
                if j in adj[i]:  
                    temp -= 1
                max_len = max(max_len, temp)
        
        return max_len
