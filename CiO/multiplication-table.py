def checkio(first, second):
    first = bin(first)[2:]
    second = bin(second)[2:]
    AND = [int(''.join(str(int(s)*int(f)) for s in second), 2) for f in first]
    OR = [int(''.join(max(s, f) for s in second), 2) for f in first]
    XOR = [int(''.join(str(int(s != f)) for s in second), 2) for f in first]
    return sum(AND + OR + XOR)
