class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        ans = [set() for _ in range(n)]
        indegree = [0 for _ in range(n)]

        for F, T in edges:
            adjList[F].append(T)
            indegree[T] += 1

        q = []
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.pop(0)
            for to in adjList[node]:
                ans[to] = ans[to].union(ans[node])
                ans[to].add(node)
                indegree[to] -= 1
                if indegree[to] == 0:
                    q.append(to)

        for i in range(len(ans)):
            ans[i] = sorted(list(ans[i]))
        return ans

                

