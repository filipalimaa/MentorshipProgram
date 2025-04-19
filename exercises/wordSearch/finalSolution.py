def exist(word, board):
    
    # Verificação Horizontal:
    for line in board: # Para cada linha horizontal da matriz
        for j in range(len(line) - len(word) + 1): # Iterar para cada posição num range que corresponda ao tamanho da word
            result = True
            print(line[j])
            for k in range(len(word)): # Iterar para cada posição da word
                if line[j + k] != word[k]: # Comparar cada letra da word com a sequência de letras na linha da matriz que esteja a começar na posição j
                    result = False
                    break
            if result:
                return True
            
    # Verificação Vertical:
    for col in range(len(board[0])): # Para cada linha vertical da matriz
        for row in range(len(board) - len(word) + 1): # Iterar cada linha com o mesmo tamanho que a word
            result = True
            print(board[row])
            for k in range(len(word)):
                if board[row + k][col] != word[k]: # Comparar cada letra da word com as letras das várias linhas da mesma coluna
                    result = False
                    break
            if result:
                return True
    
    return False

# Use Example:
word = "FCE"
board = [["A","B","C","E"],
         ["S","F","C","K"],
         ["A","D","E","E"]]
print(exist(word, board))