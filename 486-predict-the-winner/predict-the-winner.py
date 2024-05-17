class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def gamePlay(l, r, turn):
            if l == r:
                if turn:
                    return [nums[l], 0]
                else:
                    return [0, nums[l]]
            if turn:
                left =  gamePlay(l+1, r, not turn)
                right =  gamePlay(l, r-1, not turn)

                left[0] += nums[l] 
                right[0] += nums[r]

                if left[0] > right[0]:
                    return left
                else:
                    return right
            else:
                

                left =  gamePlay(l+1, r, not turn)
                right =  gamePlay(l, r-1, not turn)

                left[1] += nums[l] 
                right[1] += nums[r]

                if left[1] > right[1]:
                    return left
                else:
                    return right
        game = gamePlay(0, len(nums)-1, True)

        if game[0] >= game[1]:
            return True
        else:
            return False
    



            


                