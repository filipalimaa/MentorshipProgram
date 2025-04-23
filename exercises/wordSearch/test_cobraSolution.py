from cobraSolution import exist

## Definição de vários testes: 1º em caso de existência, para perceber se o código encontra de facto palvras válidas no board; 2º em caso de inexistência da word, ou seja, para o caso em que as letras existam no board, mas não formam a palavra
## 3º para um caso minimalista, para garantir que ele aceita qualquer tamanho da palavra; 4º testar quando realmente as letras da palavra não existem no board, para verificar se ignora letras inexistentes

## Outros possíveis testes: boards maiores ou vazios (?)

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
