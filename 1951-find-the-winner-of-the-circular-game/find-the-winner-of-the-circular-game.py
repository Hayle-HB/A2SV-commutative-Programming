class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]


        queue = deque(arr)

        while len(queue) != 1:
            
            for i  in range(k-1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue.popleft()
        

        