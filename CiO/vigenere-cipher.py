def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = []
    # get letters from both words
    for d, e in zip(old_decrypted, old_encrypted):
        # get their Unicode code point
        v = list(map(ord, [d, e]))
        # key is the offset between both and must be > 65 (uppercase A)
        key += [(v[0] - v[1]) % 26+65]

    keyLen = len(key)
    if keyLen < len(new_encrypted):
        # find the longest repeating pattern. 
        # Fails if the pattern is huge and starts repeating close to the end
        for i in range(keyLen//2, 1, -1):
            if key[:i] == key[i:2*i]:
                key = key[:i]
                break
        # extend the key just a bit
        key *= 100

    new_decrypted = ''
    for k, l in zip(key, new_encrypted):
        new_decrypted += chr(((ord(l)+k) % 26)+65)
    return new_decrypted
