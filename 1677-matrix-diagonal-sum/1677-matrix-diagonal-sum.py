class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        total = 0

        for i in range(size):
            total += mat[i][i]
            total += mat[i][size-1-i]
        
        if size % 2 == 1:
            total -= mat[size //2][size //2]
        
        return total