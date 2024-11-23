class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n, left, max_len  = len(nums), 0, 0

        for right in range(n):

            if nums[right] == 0:
                k -= 1
            
            while k < 0 and left <= right:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

        