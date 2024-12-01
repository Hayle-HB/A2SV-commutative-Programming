class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal = 0

        currSum = 0
        for num in nums:
            currSum += num

            if currSum < 1:
                temp = minVal
                minVal += abs(currSum) + 1
                currSum += minVal - temp
        
        return minVal if minVal > 0 else 1

        