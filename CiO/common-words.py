def checkio(a, b):
    return ','.join(x for x in sorted(a.split(',')) if x in sorted(b.split(',')))
