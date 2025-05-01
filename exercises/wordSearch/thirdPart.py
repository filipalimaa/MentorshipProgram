def exist(word, board):

    # Verificação Horizontal:
    for line in board:
        for j in range(len(line) - 1):
            print(line[j])
            if line[j] == word[0]:
                print(line(j + 1))
                if line[j + 1] == word[1]:
                    return True
                print()

    # Verificação Vertical:
    for col in range(len(board[0])):
        for row in range(len(board) - 1):
            print(board[row])
            if board[row][col] == word[0]:
                if board[row + 1][col] == word[1]:
                    return True
                print()

    return False


# Use Example:
word = "KE"
board = [["A", "B", "C", "E"], ["S", "F", "C", "K"], ["A", "D", "E", "E"]]
print(exist(word, board))
