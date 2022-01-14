from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        q = deque()
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    fresh +=1
        
        minute = 0
        
        prev =fresh
        
        while q:
            i, j, minute = q.popleft()
            
            if grid[i][j] == 2:
                for r,c in [(i, j-1),(i, j+1), (i-1, j), (i+1, j)]:
                    if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                        fresh -=1
                        grid[r][c] = 2
                        q.append((r,c, minute+1))
        if fresh > 0:
            return -1
        else:
            return minute