class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for row in matrix:
            for i in range(len(row)-1):
                row[i+1] += row[i]

        count = 0
        for t in range(len(matrix)):
            for j in range(t, -1, -1):
                if t == j:
                    current = matrix[t][:]
                else:
                    current = [current[i]+matrix[j][i] for i in range(len(matrix[0]))]
                seen_mat = {0: 1}
                for v in current:
                    if v - target in seen_mat:
                        count += seen_mat[v - target]
                    seen_mat[v] = seen_mat.get(v, 0) + 1
                    
        return count