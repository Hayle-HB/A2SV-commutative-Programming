class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        Min = arr[1]-arr[0]

        for i in range(len(arr)-1):
            Min = min(Min, arr[i+1]-arr[i])



        for idx in range(len(arr)-1):
            if arr[idx+1] - arr[idx] == Min:
                ans.append([arr[idx], arr[idx+1]])
        
        return ans
        