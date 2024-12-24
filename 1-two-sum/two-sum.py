class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        answer = []
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in hash:
                answer.extend([hash[comp], idx])
                break
            hash[num] = idx
        
        return answer

        