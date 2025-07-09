def cutRod(price):
    rod_length = len(price)
    return rod(price, rod_length)

def rod(price, remain):
    if remain == 0:
        return 0
    
    max_value = float('-inf')
    
    for i in range(1, remain + 1):
        value = price[i -1] + rod(price, remain - i)
        max_value = max(max_value, value)
    
    return max_value