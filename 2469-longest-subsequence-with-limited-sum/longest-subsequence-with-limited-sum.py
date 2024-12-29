class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        

        def bs(q):
            left, right = 0, len(nums)-1

            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] > q:
                    right = mid - 1
                else:
                    left += 1
            return left
        return [bs(q) for q in queries]