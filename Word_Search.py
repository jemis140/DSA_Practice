class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row,col,word):
                    return True
        
        return False
    
    def backtrack(self, row, col, suffix):
        
        if len(suffix) == 0:
            return True
        
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret

            
            