class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs) == 0:
            return 0
        def can_represent(bomb1, bomb2):
            x1,  y1, r1 = bomb1
            x2, y2, r2 = bomb2

            distance = sqrt((x2-x1)**2 + (y2 - y1) ** 2)

            return distance <= r1
        
        adj = defaultdict(list)


        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i != j and can_represent(bombs[i], bombs[j]):
                    adj[i].append(j)
        
        def dfs(node, visited):
            stack = [node]
            count = 0

            while stack:
                curr = stack.pop()
                if curr not in visited:
                    count += 1
                    visited.add(curr)
                for next in adj[curr]:
                    if next not in visited:
                        stack.append(next)
            return count
        

        answer = 0
        
        for i in range(n):
            visited = set()
            answer = max(answer, dfs(i, visited))
        
        return answer





            
        