class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0][0]
        y = edges[0][1]
        z = edges[1][1]
        w = edges[1][0]

        if x == z or x == w:
            return x
        return y