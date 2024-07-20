class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0] * n
        
        for u, v in relations:
            adj[u-1].append(v-1)
            indegree[v-1] += 1
        
        memo = {}
        
        def dp(node):
            if node in memo:
                return memo[node]
            
            max_time = time[node]
            
            for next_node in adj[node]:
                max_time = max(max_time, dp(next_node) + time[node])
            
            memo[node] = max_time
            return memo[node]
        
        result = 0
        for i in range(n):
            if indegree[i] == 0:
                result = max(result, dp(i))
        
        return result