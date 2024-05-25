class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
            if len(arr) < 3:
                return sum(arr)
            prefix  = [0] * (len(arr) +1)
        
            for i in range(len(arr)):
                prefix[i+1] = arr[i] + prefix[i]
            print(prefix)

            
            Sum = 0

            for i in range(1, len(arr)+1):
                for j in range(i, len(arr)+1, 2):
                  Sum += prefix[j] - prefix[i-1]
            return Sum