class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1: 
            return 0
        Mid =math.pow(2,n-1)//2
        if k<=Mid:
            return self.kthGrammar(n-1,k)
        else:
            return 1-self.kthGrammar(n-1,k-Mid ) 