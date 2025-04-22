from cobraSolution import exist

def test_exist_true():
    
    board = [["A","B","C","E"],
             ["S","F","C","K"],
             ["A","D","E","E"]]
    
    word = "BCCE"
    assert exist(board, word) == True

def test_exist_false():
    
    board = [["A","B","C","E"],
             ["S","F","C","K"],
             ["A","D","E","E"]]
    
    word = "ABCD"
    assert exist(board, word) == False

def test_exist_two_letter():
    
    board = [["A","B","C","E"],
             ["S","F","C","K"],
             ["A","D","E","E"]]
    
    word = "FD"
    assert exist(board, word) == True

def test_exist_not_present():
    
    board = [["A","B","C","E"],
             ["S","F","C","K"],
             ["A","D","E","E"]]
    
    word = "ILMN"
    assert exist(board, word) == False
