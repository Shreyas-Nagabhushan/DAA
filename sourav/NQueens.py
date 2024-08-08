class Board:
    def __init__(self, size):
        self.size = size
    

    def nqueens(self):
        n = self.size
        board = [[" " for _ in range(n)] for _ in range(n)]
        solutions = []

        def is_safe(board, r,c):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "Q" and (i == r or j == c or abs(i-r) == abs(j-c)):
                        return False
            
            return True

        def nqueens_recursive(board, r, c,  queens):
            nonlocal solutions
            board = [[board[i][j] for j in range(n)] for i in range(n)]

            if is_safe(board, r, c):
                board[r][c] = "Q"
                queens += 1

                if queens == n:
                    solutions+= [board]
                
                for i in range(n): 
                    nqueens_recursive(board, r+1, i, queens)
        
        for i in range(n):
            nqueens_recursive(board, 0, i, 0)
    
        for solution in solutions:
            for row in solution:
                print(row)
            print()
        
        print("Total solutions: ", len(solutions))

Board(int(input("Enter board size: "))).nqueens()
