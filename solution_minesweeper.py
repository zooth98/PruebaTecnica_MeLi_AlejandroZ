def count_neighbouring_mines(board: list) -> list:
    """
    Counts neighbouring mines for each cell in a Minesweeper board.
    Parameters:
    board (list): A 2D list where 0 represents an empty space and 1 represents a mine
    Returns:
    list: A 2D list where each cell contains the count of neighbouring mines,
    or 9 if the cell contains a mine
    """

    #Implementation
    #Recorremos la matriz y reemplazamos los 1 por 9
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 9
    
    #Iniciamos el conteo de las minas en cada posición
    count_mines = 0 #Iniciamos el contador para guardar el registro de las minas alrededor de la posición
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i-1][j-1] == 9 and board[i-1][j-1] != None:
                count_mines = count_mines + 1
            if board[i][j-1] == 9 and board[i][j-1] != None:
                count_mines = count_mines + 1
            if board[i+1][j-1] == 9 and board[i+1][j-1] != None:
                count_mines = count_mines + 1
            if board[i+1][j] == 9 and board[i+1][j] != None:
                count_mines = count_mines + 1
            if i+1 < len(board) and j+1 < len(board[i]) and board[i+1][j+1] == 9:
                count_mines = count_mines + 1
            if board[i][j+1] == 9 and i < len(board) and j+1 < len(board[i]):
                count_mines = count_mines + 1
            if board[i-1][j+1] == 9 and board[i-1][j+1] != None:
                count_mines = count_mines + 1
            if board[i-1][j] == 9 and board[i-1][j] != None:
                count_mines = count_mines + 1
        print(count_mines)        
        board[i][j] = count_mines
    print(board)
    return board
    

board = [
    [0, 1, 0],
    [1, 0, 1]
]
print(count_neighbouring_mines(board))