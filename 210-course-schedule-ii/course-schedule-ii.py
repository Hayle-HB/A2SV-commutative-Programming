class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            indegree = [0] * n
            for u, v in prerequisites:
                graph[u].append(v)
                indegree[v] += 1
            order = []
            queue = deque([i for i in range(n) if indegree[i] == 0 ])
            courseTaken = 0
            while queue:
                curr = queue.popleft()
                order.append(curr)
                courseTaken += 1
                for nighbor in graph[curr]:
                    indegree[nighbor] -= 1

                    if indegree[nighbor] == 0:
                        queue.append(nighbor)

            return order[::-1] if courseTaken == n else []
