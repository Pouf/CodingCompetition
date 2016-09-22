def longest_palindromic(text):
    s = len(text)
    for size in range(s)[::-1]:
        for index in range(s - size):
            word = text[index:index + size + 1]
            if word == word[::-1]:
                return word
