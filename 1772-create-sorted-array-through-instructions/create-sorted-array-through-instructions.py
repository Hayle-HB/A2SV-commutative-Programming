class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_value = max(instructions)
        fenwick_tree = FenwickTree(max_value)
        total_cost = 0
        
        for i, num in enumerate(instructions):
            count_less = fenwick_tree.query(num - 1)
            count_greater = i - fenwick_tree.query(num)
            total_cost += min(count_less, count_greater)
            total_cost %= MOD
            fenwick_tree.update(num, 1)
        
        return total_cost
