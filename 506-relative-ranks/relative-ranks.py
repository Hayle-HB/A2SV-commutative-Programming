from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}

        for i, s in enumerate(score):
            dic[s] = i
        
        dic = sorted(dic.items(), reverse=True)

        ans = [0] * len(score)

        for i, (score, index) in enumerate(dic):
            if i == 0:
                ans[index] = 'Gold Medal'
            elif i == 1:
                ans[index] = 'Silver Medal'
            elif i == 2:
                ans[index] = 'Bronze Medal'
            else:
                ans[index] = str(i + 1)

        return ans
