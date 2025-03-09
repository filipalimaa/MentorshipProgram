from functools import cmp_to_key

"""Neste exercício pretende-se organizar os números de uma lista, de forma a obter o maior número possível. Correndo o risco de ser um número muito elevado, devolver em string.""" 

# 1. Ordenar os números como strings
def comparar(x, y):
    if x + y > y + x:
        return -1 # x vem primeiro que y
    else:
        return 1 # y vem primeiro que x

def largestNumber(nums):
    strNums = list(map(str, nums)) # Conersão dos números em string
    
    strNums.sort(key=cmp_to_key(comparar)) # Ordenar os números, de acordo com a comparação prévia
    
    return "".join(strNums)

nums = [2, 10]
print(largestNumber(nums))

nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))