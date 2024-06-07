from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num5 = 0
        num10 = 0

        for bill in bills:
            if bill == 5:
                num5 += 1
            elif bill == 10:
                if num5 == 0:
                    return False
                num5 -= 1
                num10 += 1
            else:  
                if num10 > 0 and num5 > 0:
                    num10 -= 1
                    num5 -= 1
                elif num5 >= 3:
                    num5 -= 3
                else:
                    return False
        return True
