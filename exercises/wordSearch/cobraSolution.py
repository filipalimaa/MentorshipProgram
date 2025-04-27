def exist(board, word):

    def search(row, col, index, visited): # row e col é a posição atual, index é a posição da letra atual
        if index == len(word): # Verificar se já foram percorridas todas as letras da word
            return True

        if (
            row < 0 or row >= len(board) or # As primeiras condições para validar se a posição (row, col) está fora da matriz
            col < 0 or col >= len(board[0]) or
            (row, col) in visited or # Verificar se a posição já foi "analisada"
            board[row][col] != word[index] # Verificar se a letra da matriz é diferente que a letra na posição atual da word
        ):
            return False # Se alguma destas condições se verificar, devolve logo False
        
        visited.add((row, col))  # Se nenhuma das condições de verificar fazemos um append a um array com letras já "verificadas"

        if (
            search(row + 1, col, index + 1, visited) or # Verificar na mesma coluna, na linha em baixo
            search(row - 1, col, index + 1, visited) or # Verificar na mesma coluna, na linha em cima
            search(row, col + 1, index + 1, visited) or # Verificar na mesma linha, coluna da direita
            search(row, col - 1, index + 1, visited) # Verificar na mesma linha, coluna da esquerda
        ):
            return True # Se encontrar cada letra da word (index + 1), devolve true

        visited.remove((row, col)) # Se a palavra não foi encontrada para a posição (row, col), tira-se do array, para voltar outra vez a ser analisada na próxima try
        return False

    for row in range(len(board)): # Para cada linha da matriz
        for col in range(len(board[0])): # Para cada coluna da matriz
            if board[row][col] == word[0]: # Tentamos encontrar a primeira letra da ord
                if search(row, col, 0, set()): # Encontrando a primeira letra, usamos a função search p/ encontrar o resto nas outras direções
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

                        