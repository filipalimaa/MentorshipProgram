def romanToInt(s):
    # Vou criar primeiro um dicionário com a numeração romana
    romanValues = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prevValue = 0 # Guardar o valor anterior para verificar a subtração
    
    for char in reversed(s):
        value = romanValues[char]
        
        if value < prevValue:
            total -= value # Sendo menor, subtrai
        else:
            total += value # Sendo maior, soma
        
        prevValue = value
    
    return total

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
print(romanToInt("MCMXCV"))