class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        Copy = heights.copy()
        Copy.sort()
        print(Copy)

        count = 0

        for i in range(len(Copy)):
            if Copy[i] != heights[i]:
                count += 1
        
        return count
        