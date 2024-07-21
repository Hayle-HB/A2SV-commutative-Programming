class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], time: List[int]) -> int:
            adj = defaultdict(list)

            for u, v in edges:
                adj[u-1].append(v-1)

            memo = {}

            def dp(node):
                if node in memo:
                    return memo[node]
                res = time[node]

                for next in adj[node]:
                    res = max(res, time[node] + dp(next))
                
                memo[node] = res
                return memo[node]
            res = 0
            for i in range(n):
                    res = max(res, dp(i))
            return res 