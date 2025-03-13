class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        if n == 0:
            return 1

        

        def help(x, n):
            if n == 1:
                return x
            elif n == 0:
                return 0
            
            if n % 2 == 0:
                res =  help(x, n // 2)
                return res * res
            else:
                res = help(x, n // 2)
                return res * res * x
        return help(x, n)

                

        