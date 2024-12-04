class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: Calculate the prefix products
        result[0] = 1  # There's no element before the first element
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        print(result)
        # Step 2: Calculate the suffix products and update result
        suffix = 1  # There's no element after the last element
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]  # Update the suffix for the next iteration

        return result