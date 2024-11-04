class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(int)
        for i in time:
            d[i%60]+=1
        l=[i for i in d.keys()]
        print(l)
        res=0
        for i in l:
            if i not in d:
                continue
            k=(60-i)%60
            if k==30:
                res+=(d[k]*(d[k]-1))//2
            elif k==0:
                res+=(d[0]*(d[0]-1)) //2
                d.pop(0)
            elif k in d:
                res+=d[k]*d[i]
                d.pop(k)
                d.pop(i)
        return res        