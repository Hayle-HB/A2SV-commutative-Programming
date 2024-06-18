class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        dic = sorted(zip(difficulty, profit))
        worker.sort()
        maxPro = 0
        currMax = 0
        idx = 0
        for work in worker:

            while idx < len(dic) and dic[idx][0] <= work:
                currMax = max(currMax, dic[idx][1])
                idx += 1
            maxPro += currMax

        return maxPro

            



        