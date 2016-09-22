def translate(phrase):
    code, skip = '', 0
    for letter in phrase:
        if skip:
            skip -= 1
        else:
            code += letter
            skip = [1, 2, 0][(letter in 'aeiouy') - (letter is ' ')]
    return code
