class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        def bound(i, j):
            return (0 <= i and i < n) and (0 <= j and j  < m)
        
        Dup =   [-1, 1]
        Ddown = [1, -1]
        right = [0, 1]
        down =  [1, 0]

        turn = True
        x, y = 0, 0
        ans = []
        t = 100
        while True:
            if not bound(x, y):
                break
            # up diagonal move
            if turn:
                while bound(x, y):
                    ans.append(mat[x][y])
                    x += Dup[0]
                    y += Dup[1]

                x -= Dup[0]
                y -= Dup[1]

                nx = x + right[0]
                ny = y + right[1]

                if bound(nx, ny):
                    x = x + right[0]
                    y = y + right[1]
                else:
                    x = x + down[0]
                    y = y + down[1]
                turn = False

                    
            # down diagonal move

            if not turn:

                while bound(x, y):
                    ans.append(mat[x][y])
                    x = x + Ddown[0]
                    y = y + Ddown[1]
                x -= Ddown[0]
                y -= Ddown[1]

                nx = x + down[0]
                ny = y + down[1]
                if bound(nx, ny):
                    x = x + down[0]
                    y = y + down[1]
                else:
                    x += right[0]
                    y += right[1]
                turn = True


        return ans