import re
import string


def checkio(url):
    scheme, remainingStuff = url.split('//')
    new = scheme.lower() + '//'
    if '/' in remainingStuff:
        replaceable = string.ascii_letters + string.digits + '-_~.'
        remainingStuff = re.sub('/[^/]*/\.{2}', '', remainingStuff.lower())
        host, *remainingStuff = remainingStuff.split('/')
        new += host
        for block in remainingStuff:
            triplets = re.findall('%[a-zA-Z0-9]{2}', block)
            for t in set(triplets):
                newT = (chr(int(t[1:], 16)))
                newT = newT.lower() if newT in replaceable else t.upper()
                block = block.replace(t, newT)
            new += '/' + block
    else:
        new += remainingStuff.lower()
    new = re.sub(':80(?!\d)', '', new)
    while '/./' in new:
        new = new.replace('/./', '/')
    return new
