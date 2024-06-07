class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > current:
                arrows += 1
                current = points[i][1]
        
        return arrows

# [        [1, 2]          [2, 3]             [3, 4]                [4, 5]]
# [        [1, 6]          [2, 8]             [7, 12]               [10, 16]]

# 