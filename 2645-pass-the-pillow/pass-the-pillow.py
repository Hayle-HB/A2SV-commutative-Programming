class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        move = time // (n - 1)
        remain = time % (n-1)

        if move % 2 == 0:
            return 1 + remain
        else:
            return n  -  remain
            
            
            





        