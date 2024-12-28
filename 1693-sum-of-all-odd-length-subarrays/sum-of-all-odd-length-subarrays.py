class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for i in range(n):
            total_subarr= (i+1) * (n-i)

            odd_subarr = (total_subarr + 1 )// 2

            total += arr[i] * odd_subarr
        return total