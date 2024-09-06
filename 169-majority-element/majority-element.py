class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        curr = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                curr += 1
            else:
                if curr > n // 2:
                    return nums[i-1]
                else:
                    curr = 1
        return  nums[-1]

            