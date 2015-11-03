def checkio(n, m):
    return bin(n | m).count('1') - bin(n & m).count('1')
