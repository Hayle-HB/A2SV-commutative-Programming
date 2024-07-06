class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(node):
            time = 0
            visited.add(node)

            for next in adj[node]:
                if next not in visited:
                    child = dfs(next)

                    if child > 0 or hasApple[next]:
                        time += child + 2
                
            return time
        
        return dfs(0)
        