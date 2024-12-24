class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)

        for i, num in enumerate(nums):
            if num not in hash:
                hash[num] = (i, -1)
            else:
                hash[num] = (hash[num][0], i)
        
        nums.sort()

        left, right = 0, len(nums)-1
        answer = []
        print(hash)
        while left < right:
            if nums[left] + nums[right] == target:
                idx1, idx2 = hash[nums[left]]
                idx3, idx4 = hash[nums[right]]
                if idx1 != -1:
                    answer.append(idx1)
                if idx2 != -1:
                    answer.append(idx2)
                if idx3 != -1:
                    answer.append(idx3)
                if idx4 != -1:
                    answer.append(idx4)
                
                break
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return list(set(answer))
