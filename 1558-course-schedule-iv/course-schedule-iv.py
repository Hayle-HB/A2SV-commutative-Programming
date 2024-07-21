class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = [0] * n
        
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0])
        group_order = []
        
        while queue:
            group = []
            for _ in range(len(queue)):
                node = queue.popleft()
                group.append(node)
                for next_node in adj[node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)
            group_order.append(group)
        
        reachable = [[False] * n for _ in range(n)]
        
        for group in group_order:
            for node in group:
                reachable[node][node] = True  
                for next_node in adj[node]:
                    for i in range(n):
                        if reachable[i][node]:
                            reachable[i][next_node] = True
        
        ans = []
        for u, v in queries:
            ans.append(reachable[u][v])
        
        return ans
