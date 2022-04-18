class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n, ans = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:  
                    ## Cases with first row or first col
                    # The 1 cells are square on its own               
                    # Other cells
                    if i==0 or j==0:
                        ans += 1
                    else:
                        #check surrounding elements 
                        #get minumum value of surrounding elemnts because if one of the surrounding elements is 0 
                        # then it will not increase size of square and 
                        # we add 1 because cell itself is square of 1*1
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
                        ans += matrix[i][j]
        return ans