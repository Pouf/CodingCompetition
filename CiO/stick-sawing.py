def checkio(number):
    n, root, total, smallest, result = 0, number**.5, 0, 0, []
    while n < root:
        while total < number:
            n += 1
            smallest += n
            total += smallest
            result.append(smallest)
        while total > number:
            total -= result.pop(0)
        if total == number:
            return result
    else:
        return []
