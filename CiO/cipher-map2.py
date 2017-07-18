def recall_password(cipher_grille, ciphered_password):
    result = ''

    for rotation in range(4):
        for line in range(4):
            for c in range(4):
                if cipher_grille[line][c] == 'X':
                    result += ciphered_password[line][c]
        cipher_grille = list(zip(*reversed(cipher_grille)))

    return result
