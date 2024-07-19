class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in richer:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(n) if in_degree[i] == 0]) 
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for next in graph[node]:
                in_degree[next] -= 1
                if in_degree[next] == 0:
                    queue.append(next)
        
        ans = list(range(n))
        
        for node in order:
            for next in graph[node]:
                if quiet[ans[node]] < quiet[ans[next]]:
                    ans[next] = ans[node]
                    
        return ans