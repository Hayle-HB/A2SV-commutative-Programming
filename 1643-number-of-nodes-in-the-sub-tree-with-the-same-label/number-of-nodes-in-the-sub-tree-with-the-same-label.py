class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        count = [defaultdict(int) for _ in range(n)]
        visited = set()
        
        def dfs(node):
            visited.add(node)
            count[node][labels[node]] += 1
            for neighbor in adj[node]:
                if neighbor not in visited:
                    child_count = dfs(neighbor)
                    for char, cnt in child_count.items():
                        count[node][char] += cnt
            return count[node]
        
        dfs(0)
        return [count[i][labels[i]] for i in range(n)]
