class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = 0
        n = len(customers)
        waiter = 0
        for i in range(n):
            if waiter < customers[i][0]:
                waiter = customers[i][0]
            waiter += customers[i][1]
            waiting_time += (waiter - customers[i][0])
        return waiting_time / n
