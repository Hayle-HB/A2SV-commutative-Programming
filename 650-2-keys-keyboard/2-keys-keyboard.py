class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        num_A = 1
        copy = 1
        while num_A < n:        
            if n % num_A == 0:
                copy = num_A
                num_A += copy
                count += 1
            else:
                num_A += copy
            count += 1
        return count

