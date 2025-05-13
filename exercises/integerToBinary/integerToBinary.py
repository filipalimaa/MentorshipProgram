# Conversion integer number to binary
def integer_to_binary(number):
    if number == 0:
        return '0'
    if number == 1:
        return '1'
    
    return integer_to_binary(number // 2) + str(number % 2)