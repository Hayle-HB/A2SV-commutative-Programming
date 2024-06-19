class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [-1] * (n + 1)
        

        def dfs(node, c):

            color[node] = c
            
            for neighbor in graph[node]:
                if color[neighbor] == color[node]:
                    return False
                elif color[neighbor] == -1:
                    if not dfs(neighbor, 1 -c):
                        return False
            return True
        
        for i in range(1, n + 1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True