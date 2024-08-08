def is_safe(board, i, j):
    #checking the current row on left side 
    for k in range(j):
        if board[i][k] == 1: return False 
    #checking current col from up 
    for k in range(i):
        if board[k][j] == 1: return False 
    
    #checking left upper diagonal
    r, c = i-1, j-1 
    while r>=0 and c>=0:
        if board[r][c] == 1: return False 
        r -= 1 
        c -= 1 

    #checking right upper diagonal
    r, c = i-1, j+1 
    while r>=0 and c<len(board[0]):
        if board[r][c] == 1: return False 
        r -= 1 
        c += 1 
    
    return True 



def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    def backtrack(board, row):
        if row == len(board):
            for i in board:
                print(i)
            print()
            return 
        
        for c in range(len(board[0])):
            if is_safe(board, row, c):
                board[row][c] = 1 
                backtrack(board, row+1)
                board[row][c] = 0 
    
    backtrack(board, 0)

nqueens(4)