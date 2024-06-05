class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0

        while target != 0:
            if maxDoubles != 0:
                if target <= 1:
                    break
                if target % 2 != 0:
                    move += 1
                
                target = target // 2
                move += 1
                maxDoubles -= 1
            else:
                break
        
        return move + target - 1

        