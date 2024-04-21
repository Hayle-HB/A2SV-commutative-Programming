class Solution:
    def pivotInteger(self, n: int) -> int:
        x=sqrt(n*(n+1)/2)
        return int(x) if x==int(x) else -1
        