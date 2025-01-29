class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        a_idx, b_idx = len(a)-1, len(b)-1
        rem = 0
        while a_idx >=0  and b_idx >= 0:
            curr_sum = int(a[a_idx]) + int(b[b_idx]) + rem

            if curr_sum == 2:
                rem = 1
                curr_sum = 0
            elif curr_sum == 3:
                curr_sum = 1
                rem = 1
            else:
                rem = 0
            answer.append(str(curr_sum))
            a_idx -= 1
            b_idx -= 1
        while a_idx >= 0:
            curr_sum = int(a[a_idx]) + rem
            
            if curr_sum == 2:
                rem = 1
                curr_sum = 0
            elif curr_sum == 3:
                curr_sum = 1
                rem = 1
            else:
                rem = 0
            a_idx -= 1
            answer.append(str(curr_sum))
        while b_idx >= 0:
            curr_sum = int(b[b_idx]) + rem

            if curr_sum == 2:
                rem = 1
                curr_sum = 0
            elif curr_sum == 3:
                curr_sum = 1
                rem = 1
            else:
                rem = 0

            b_idx -= 1
            answer.append(str(curr_sum))
        
        if rem:
            answer.append(str(rem))
        return ''.join(answer)[::-1]
            






        