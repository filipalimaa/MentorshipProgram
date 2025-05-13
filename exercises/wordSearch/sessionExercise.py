def exist():
    word = "KE"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "K"], ["A", "D", "E", "E"]]

    for line in board:
        for j in range(len(line) - 1):
            print(line[j])
            if line[j] == word[0]:
                print(line(j + 1))
                if line[j + 1] == word[1]:
                    return True
                print()


print(exist())
