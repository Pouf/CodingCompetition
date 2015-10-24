def checkio(number):
    pNew = 0
    pTotal = 0
    while number > 0:
        if number <= pTotal:
            return pTotal
        pNew += 1
        if number < pTotal + pNew:
            return pTotal + max(number - pTotal, 0)
        pTotal += pNew
        number -= pTotal
    return pTotal  
