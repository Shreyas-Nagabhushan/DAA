def is_safe(board,  r, c):
    for i in range(r):
        if board[i][c] == 'Q':
            return False 
    for i in range(c):
        if board[r][i] == 'Q':
            return False 

    i = r-1 
    j = c-1
    while i >= 0 and j >= 0 :
        if board[i][j] == 'Q':
            return False 
        i -= 1
        j -= 1 
    

def nqueens(board, row, n):
    if row == n:
        print(board)
        return 
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            nqueens(board, row+1, n)
            board[row][col] = '.'

#O(n!)