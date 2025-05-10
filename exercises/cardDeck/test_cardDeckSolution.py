from cardDeckSolution import countingCards
<<<<<<< HEAD
<<<<<<< HEAD
from cardDeckSolution import counting_Cards


def test_example1():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = [
        "6",
        "7",
        "3",
        "4",
        "4",
        "4",
        "4",
        "5",
        "5",
        "3",
        "4",
        "7",
        "4",
        "6",
        "6",
        "2",
        "3",
        "3",
        "5",
        "4",
        "4",
        "2",
        "7",
        "7",
    ]

    assert countingCards(baralho, gaveta) == 2
    assert counting_Cards(baralho, gaveta) == 2


def test_example2():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = [
        "7",
        "3",
        "4",
        "4",
        "4",
        "4",
        "5",
        "5",
        "3",
        "4",
        "7",
        "4",
        "2",
        "3",
        "3",
        "5",
        "4",
        "4",
        "2",
        "7",
        "7",
    ]

    assert countingCards(baralho, gaveta) == 0
    assert counting_Cards(baralho, gaveta) == 0


def test_example3():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = []

    assert countingCards(baralho, gaveta) == 0
    assert counting_Cards(baralho, gaveta) == 0
=======
=======
from cardDeckSolution import counting_Cards
>>>>>>> 7851fdf (test: add alternative function solution for the cardDeck for pytest)

def test_example1():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = ["6","7", "3","4", "4", "4", "4","5","5","3", "4", "7", "4","6", "6", "2","3","3","5", "4", "4","2","7","7"]
    
    assert countingCards(baralho, gaveta) == 2
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5d29d9 (test: create first true test)
=======
=======
    assert counting_Cards(baralho, gaveta) == 2
>>>>>>> 7851fdf (test: add alternative function solution for the cardDeck for pytest)

def test_example2():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = ["7", "3","4", "4", "4", "4","5","5","3","4", "7", "4", "2","3","3","5", "4", "4","2","7","7"]
    
    assert countingCards(baralho, gaveta) == 0
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a82afc4 (test: create first false test)
=======
=======
    assert counting_Cards(baralho, gaveta) == 0
>>>>>>> 7851fdf (test: add alternative function solution for the cardDeck for pytest)

def test_example3():
    baralho = ["2", "3", "4", "5", "6", "7"]
    gaveta = []
    
    assert countingCards(baralho, gaveta) == 0
<<<<<<< HEAD
>>>>>>> 54018f5 (test: create false test with empty array)
=======
    assert counting_Cards(baralho, gaveta) == 0
>>>>>>> 7851fdf (test: add alternative function solution for the cardDeck for pytest)
