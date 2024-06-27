class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)-2
        graph = defaultdict(list)

        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        for val in graph:
            if len(graph[val]) != 1:
                return val
        return 0