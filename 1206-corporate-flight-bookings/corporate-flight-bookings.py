class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer=[0]*(n+1)
        for interval in bookings:
            answer[interval[0]-1]+=interval[2]
            answer[interval[1]]-=interval[2]
        s=0
        for idx in range(n):
            s+=answer[idx]
            answer[idx]=s
        return answer[:n]