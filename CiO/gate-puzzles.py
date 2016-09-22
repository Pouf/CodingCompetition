from string import punctuation

def find_word(message):
    msg = ''.join(l for l in message.lower() if not l in punctuation).split()
    lMessage = len(msg)
    scores = msg[:]

    for i, word in enumerate(msg):
        lWord = len(word)
        likeness = 0
        for each in msg:
            likeness += word[0] == each[0]
            likeness += word[-1] == each[-1]

            lEach = len(each)
            likeness += 3 * min(lWord, lEach) / max(lWord, lEach)

            common = set(word) & set(each)
            unique = set(word) | set(each)
            likeness += 5 * len(common) / len(unique)
        scores[i] = [likeness, word]

    winner = sorted(scores, key=lambda i:i[0])[-1][1]
    return winner
