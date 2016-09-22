def checkio(text, word=''):
    if not word:
        text, word = text

    text = text.replace(' ', '').lower()
    lines = text.split('\n')
    reversed = 0

    if not word in text:
        reversed = 1
        longest = max(map(len, lines))
        height = len(lines)
        lines = [''.join(lines[i].ljust(longest)[y] for i in range(height)) for y in range(longest)]
        text = '\n'.join(lines)

    absolute = text.index(word)
    line = text.count('\n', 0, absolute)
    start = lines[line].index(word)
    line += 1
    if reversed:
        return [start+1, line, start+len(word), line]
    return [line, start+1, line, start+len(word)]
