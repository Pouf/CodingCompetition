import re


def checkio(text):
    isOne = 0
    text = re.findall('[a-z]\w{1,}', text.lower())
    for w in text:
        a = w[::2]
        b = w[1::2]
        if a[0] in 'aeiouy':
            a, b = b, a
        if re.findall('^[aeiouy]+$',b) == [b] and not re.findall('[aeiouy]',a):
            isOne += 1
    return isOne
