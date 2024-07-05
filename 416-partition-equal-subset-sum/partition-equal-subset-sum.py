from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        nums.sort()
        
        possible_sums = {0}
        
        for num in nums:
            new_sums = []
            for ps in possible_sums:
                new_sum = ps + num
                if new_sum == target:
                    return True
                if new_sum < target:
                    new_sums.append(new_sum)
            possible_sums.update(new_sums)
        
        return False

