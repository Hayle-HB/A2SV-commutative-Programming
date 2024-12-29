class Solution:
    def minimumSumSubarray(self, nums, l, r) -> int:
        n = len(nums)
        prefix = [0] * (len(nums)+1)



        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)
        answer = float('inf')

        for i in range(len(nums)):

            for j in range(i + l, min(i + r + 1, n + 1)):

                curr = prefix[j] - prefix[i]
       
                if curr > 0:
                    answer = min(answer, curr)

        return answer if answer != float('inf') else -1
        