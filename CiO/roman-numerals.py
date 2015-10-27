def checkio(n):
    M = n // 1000
    C = (n // 100) % 10
    X = (n // 10) % 10
    I = n % 10

    roman = M * 'M'
    roman += 'CM'*(C == 9) + 'D'*(4 < C < 9) + 'C'*(C % 9 % 5)
    roman += 'XC'*(X == 9) + 'L'*(4 < X < 9) + 'X'*(X % 9 % 5)
    roman += 'IX'*(I == 9) + 'V'*(4 < I < 9) + 'I'*(I % 9 % 5)

    return roman
