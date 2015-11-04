from re import findall
def checkio(s):
    s = findall("[\(\)\[\]\{\}]", s)
    keepGoing = True
    while s and keepGoing:
        keepGoing = False
        if s[0] in [']', '}', ')']: return False
        if ']' in s:
            loc = s.index(']')
            if s[loc-1] == '[':
                del s[loc]
                del s[loc-1]
                keepGoing = True
        if ')' in s:
            loc = s.index(')')
            if s[loc-1] == '(':
                del s[loc]
                del s[loc-1]
                keepGoing = True
        if '}' in s:
            loc = s.index('}')
            if s[loc-1] == '{':
                del s[loc]
                del s[loc-1]
                keepGoing = True
    if not s: return True
    return False
