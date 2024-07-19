class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([i for i in range(n) if indegree[i] == 0 ])
        courseTaken = 0
        while queue:
            curr = queue.popleft()
            courseTaken += 1
            for nighbor in graph[curr]:
                indegree[nighbor] -= 1

                if indegree[nighbor] == 0:
                    queue.append(nighbor)

        return courseTaken == n
