from unicodedata import normalize, category


def checkio(in_string):
    # normalize splits accented letters in two: letter + accent
    # category(c) 'Mn' contains every accent
    # http://www.fileformat.info/info/unicode/category/Mn/list.htm
    return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')
