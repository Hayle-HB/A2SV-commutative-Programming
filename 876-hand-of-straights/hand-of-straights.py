from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        counters = sorted(count)
        
        for hd in counters:
            if count[hd] > 0: 
                needed = count[hd]
                
                for i in range(hd, hd + groupSize):
                    if count[i] < needed:
                        return False
                    count[i] -= needed
        
        return True
