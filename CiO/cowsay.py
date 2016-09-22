import textwrap
​
​
def cowsay(text):
    longWords = filter(lambda w: len(w) > 39, text.split())
    for word in longWords:
        text = text.replace(word, word[:39]+' '+word[39:])
    lead, trail = [' '*bool(s) for s in text.split(text.strip())]
    text = lead + ' '.join(text.split())
    lines = textwrap.wrap(text, 39)
    if lead and lines[0][0] != ' ':
        lines.insert(0, ' ')
    if trail:
        lines[-1] += trail
    longest = len(max(lines, key=len))
    lines = ['{0: <{1}}'.format(l, longest) for l in lines]
​
    nbLines = len(lines)
​
    raw = '\n ' + longest * '_' + '__'
​
    for i, l in enumerate(lines):
        if nbLines == 1:
            deco = '\n<  >'
        elif i == 0:
            deco = '\n/  \\'
        elif i == nbLines-1:
            deco = '\n\\  /'
        else:
            deco = '\n|  |'
​
        raw += deco[:3] + l + deco[3:]
​
    raw += r'''
{0:-<{1}}---
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''.format(' ', longest)
    return raw
