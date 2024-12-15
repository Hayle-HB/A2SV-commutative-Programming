class Solution:
    def getDistances(self, nums: List[int]) -> List[int]:
        n, dict1 = len(nums), defaultdict(list)

        for i,v in enumerate(nums):
            dict1[v].append(i)

        arr = [0]*n 

        for key,val in dict1.items():
            pre_sum, suf_sum = 0, sum(val)
            p, s = 0, len(val)

            for i in val:
                pre_sum += i
                suf_sum -= i
                p += 1
                s -= 1
                arr[i] = -pre_sum + i*p + suf_sum - i*s

        return arr