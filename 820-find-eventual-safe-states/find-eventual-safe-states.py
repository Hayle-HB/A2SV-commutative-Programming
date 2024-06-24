from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)

        indegree = [0] * len(graph)

        for i in range(len(graph)):
            for j in adj[i]:
                indegree[j] += 1

        queue = deque()

        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        ans = []        
        
        while(queue):
            element = queue.popleft()
            ans.append(element)

            for i in adj[element]:
                if indegree[i] != 0:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        queue.append(i)

        return sorted(ans)