class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        def dfs(node, path):
            if node == n-1:
                ans.append(path)
                return
            for next in graph[node]:
                dfs(next, path + [next])

        dfs(0, [0])
        return ans

        