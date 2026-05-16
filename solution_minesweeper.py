import copy

def count_neighbouring_mines(board: list) -> list:
    """
    Counts neighbouring mines for each cell in a Minesweeper board.
    Parameters:
    board (list): A 2D list where 0 represents an empty space and 1 represents a mine
    Returns:
    list: A 2D list where each cell contains the count of neighbouring mines,
    or 9 if the cell contains a mine
    """

    #Implementacion
    
    #Reemplazamos los 1 por 9 en el tablero
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] == 1:
                board[i][j] = 9
    print(board)
        
    #Iniciamos el conteo de las minas en cada posición

    #Creamos una matriz para calcular las 8 posiciones alrededor de una casilla
    directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
    ]

    for i in range (len(board)):
        for j in range (len(board[i])):
            
            if board[i][j] == 9:
                continue
            count_mines = 0 #Iniciamos el contador para guardar el registro de las minas alrededor de la posición
            for x, y in directions:
                new_i = i + x
                new_j = j + y

                #Validamos los bordes
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[new_i]):
                    if board[new_i][new_j] == 9:
                        count_mines += 1
            board[i][j] = count_mines
    return board
    

board = [
[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 1, 0, 1],
[1, 1, 0, 0]
]
print(count_neighbouring_mines(board))