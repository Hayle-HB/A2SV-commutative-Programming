class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:

                curr_sum = a + nums[l] + nums[r]

                if curr_sum > 0: 
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    answer.append([a, nums[l], nums[r]])
                    l += 1

                    while  nums[l] == nums[l-1] and l < r:
                        l += 1
        return answer