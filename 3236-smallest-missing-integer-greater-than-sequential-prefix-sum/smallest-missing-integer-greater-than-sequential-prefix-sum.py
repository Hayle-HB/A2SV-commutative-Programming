from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the longest sequential prefix and its sum
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_sum += nums[i]
            else:
                break
        max_sum = curr_sum

        # Step 2: Sort the array
        nums.sort()

        # Step 3: Find the smallest missing integer >= max_sum
        missing = max_sum
        nums_set = set(nums)
        while missing in nums_set:
            missing += 1

        return missing
