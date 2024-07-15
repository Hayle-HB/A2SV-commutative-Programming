class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:

        if y >= x:
            return y - x
        
        queue = deque([(x, 0)])
        visit = set([x])


        while queue:
            curr , op = queue.popleft()

            next = []

            if curr % 11 == 0:
                next.append(curr // 11)
            if curr % 5 == 0:
                next.append(curr // 5)
            
            if curr > 1:
                next.append(curr - 1)
            next.append(curr + 1)


            for n in next:
                if n == y:
                    return op + 1

                if n not in visit:
                    visit.add(n)
                    queue.append((n, op + 1))
        return -1