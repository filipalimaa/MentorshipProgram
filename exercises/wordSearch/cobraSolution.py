def search(row, col, index, visited): 
    if index == len(word):
        return True

    if (
        row < 0 or row >= len(board) or 
        col < 0 or col >= len(board[0]) or
        (row, col) in visited or 
        board[row][col] != word[index]
    ):
        return False 
        
    visited.add((row, col)) 

    if (
        search(row + 1, col, index + 1, visited) or 
        search(row - 1, col, index + 1, visited) or 
        search(row, col + 1, index + 1, visited) or 
        search(row, col - 1, index + 1, visited) 
    ):
        return True 

    visited.remove((row, col))
    return False

def exist(board, word):

    def search(row, col, index, visited): 
        if index == len(word):
            return True

        if (
            row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or
            (row, col) in visited or 
            board[row][col] != word[index]
        ):
            return False 
        
        visited.add(row, col) 

        if (
            search(row + 1, col, index + 1, visited) or 
            search(row - 1, col, index + 1, visited) or 
            search(row, col + 1, index + 1, visited) or 
            search(row, col - 1, index + 1, visited) 
        ):
            return True 

        visited.remove(row, col)
        return False

    for row in range(len(board)): 
        for col in range(len(board[0])): 
            if board[row][col] == word[0]: 
                if search(row, col, 0, set()): 
                    return True

    return False

word = "BCCE"
board = [["A","B","C","E"],
         ["S","F","C","K"],
         ["A","D","E","E"]]

print(exist(board, word))

"""def exist(word, board):
    directions = [
        (0, 1),   # Direita
        (0, -1),  # Esquerda
        (1, 0),   # Baixo
        (-1, 0)   # Cima
    ]
    
    for i in range(len(board)):             # Itera pelas linhas
        for j in range(len(board[0])):      # Itera pelas colunas
            if board[i][j] == word[0]:      # Encontrou a primeira letra
                for direction in directions:
                    dx, dy = direction
                    result = True
                    
                    for k in range(1, len(word)):
                        l = i + dx * k
                        m = j + dy * k
                        
                        # Verifica se está dentro da matriz
                        if 0 <= l < len(board) and 0 <= m < len(board[0]):
                            if board[l][m] != word[k]:
                                result = False
                                break
                        else:
                            result = False
                            break
                    
                    if result:
                        return True
    return False

# Exemplo de uso:
word = "BCEK"
board = [["A","B","C","E"],
         ["S","F","C","K"],
         ["A","D","E","E"]]

print(exist(word, board))"""

                        