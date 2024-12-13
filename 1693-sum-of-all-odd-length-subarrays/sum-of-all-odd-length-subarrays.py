class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:        
        arrlen = len(arr)        
        if arrlen <= 2:
            return sum(arr)        
        if arrlen%2 == 1:
            res = 2*sum(arr)
        else:
            res = sum(arr) 
                            
        for i in range(3, arrlen, 2):       
            for j in range(0,arrlen-i+1): 
                res += sum(arr[j:j+i])  
        return res