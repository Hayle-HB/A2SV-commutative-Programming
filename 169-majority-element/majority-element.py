class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count = Counter(nums)

       answer = [num for num in count if count[num] > len(nums) // 2]
       return answer[0]

        