class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rediant = deque()
        dire = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] =='R':
                rediant.append(i)
            else:
                dire.append(i)
        while len(rediant)!=0 and len(dire)!=0:
            r = rediant.popleft()
            d = dire.popleft()
            n+=1
            if r < d:
                rediant.append(n)
            else:
                dire.append(n)
        if len(rediant) >0:
            return "Radiant"
        return "Dire"
            
        
            