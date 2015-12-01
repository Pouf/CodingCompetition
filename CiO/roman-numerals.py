def checkio(n):
    M = n // 1000
    C = (n // 100) % 10
    X = (n // 10) % 10
    I = n % 10

    roman = M * 'M'
    roman += 'CM'*(C == 9) + 'C'*(C == 4) + 'D'*(3 < C < 9) + 'C'*(C % 9 % 5 % 4)
    roman += 'XC'*(X == 9) + 'X'*(X == 4) + 'L'*(3 < X < 9) + 'X'*(X % 9 % 5 % 4)
    roman += 'IX'*(I == 9) + 'I'*(I == 4) + 'V'*(3 < I < 9) + 'I'*(I % 9 % 5 % 4)

    return roman
