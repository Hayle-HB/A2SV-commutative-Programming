
""""
             1
           1   1
          1   2   1
        1   3   3   1
       1  4   6   4   1

"""
class Solution(object):
    def getRow(self, rowIndex):
        result = [1] * (rowIndex + 1)

        for i in range(1, rowIndex + 1):
            val = result[i - 1] * (rowIndex - i + 1) / i
            result[i] = int(val)

        return result

