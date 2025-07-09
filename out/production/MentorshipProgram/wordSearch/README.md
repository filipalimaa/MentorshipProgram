Given an m X n grid of characters board and a string word, return True if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be
used more than once.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase english letters.

1. First solution: assuming that the word only exists horizontally, and assuming a specific word and board -> sessionExercise.py

2. Second solution: modify the function created in the first solution so that it can accept both variables: word vs board -> secondPart.py

3. Third solution: modify the previous function so that it can also accept the existence of the word in the vertical direction -> thirdPart.py