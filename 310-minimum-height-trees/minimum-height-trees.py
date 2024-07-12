from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        neighbors = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        leaves = deque([i for i in range(n) if indegree[i] == 1])
        
        remain_leavs = n
        while remain_leavs > 2:
            remain_leavs -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for neighbor in neighbors[leaf]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        leaves.append(neighbor)
        
        return list(leaves)
