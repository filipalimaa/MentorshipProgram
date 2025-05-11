from cutRodSolution import cutRod

def test_example1():
    assert cutRod([1, 5, 8, 9, 10, 17, 17, 20]) == 22
    
def test_example2():
    assert cutRod([3, 5, 8, 9, 10, 17, 17, 20]) == 24