class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        MaxQueue = deque()
        MinQueue = deque()

        max_len = 0

        left  = 0 

        for right in range(len(nums)):

            while MaxQueue and nums[right] > MaxQueue[-1]:
                MaxQueue.pop()
            MaxQueue.append(nums[right])

            while MinQueue and nums[right] < MinQueue[-1]:
                MinQueue.pop()
            MinQueue.append(nums[right])

            while MaxQueue[0] - MinQueue[0] > limit:
                if MaxQueue[0] == nums[left]:
                    MaxQueue.popleft()
                if MinQueue[0] == nums[left]:
                    MinQueue.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
                
                
            


            
            



        