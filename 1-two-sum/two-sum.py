class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = [(num, idx) for idx, num in enumerate(nums)]

        pair.sort(key = lambda x:x[0])

        left, right = 0, len(nums)-1

        while left < right:
            curr = pair[left][0] + pair[right][0]

            if curr == target:
                return [pair[left][1], pair[right][1]]
            elif curr > target:
                right -= 1
            else:
                left += 1
        return []
        