class Solution:
    def sinkship(self, board, i, j):
        if i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j]!='X':
            return
        
        board[i][j]='.'
        self.sinkship(board, i+1, j)
        self.sinkship(board, i-1, j)
        self.sinkship(board, i, j+1)
        self.sinkship(board, i, j-1)
    
    def countBattleships(self, board: List[List[str]]) -> int:
        no_ships=0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    no_ships+=1
                    self.sinkship(board, i, j)
        
        return no_ships
