class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # If the target is negative, it's impossible to find a solution
        if target < 0:
            return -1

        curr, max_len = 0, float('-inf')
        left = 0

        for right in range(len(nums)):
            curr += nums[right]

            # Shrink the window until curr <= target
            while curr > target and left <= right:
                curr -= nums[left]
                left += 1

            # Update max_len when a valid subarray is found
            if curr == target:
                max_len = max(max_len, right - left + 1)

        # If no valid subarray is found, return -1
        return len(nums) - max_len if max_len != float('-inf') else -1
