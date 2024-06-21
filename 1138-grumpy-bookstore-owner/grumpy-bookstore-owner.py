from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        

        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        
        
        curr_sat = 0
        max_sat = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 1:
                curr_sat += customers[i]
            
           
            if i >= minutes and grumpy[i - minutes] == 1:
                curr_sat -= customers[i - minutes]
            
            max_sat = max(max_sat, curr_sat)
        
        return total + max_sat
