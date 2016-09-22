import re


def checkio(text):
    numbers =  re.findall('(?<=\$)[^ ]*\d', text)
    for old in numbers:
        new = old.replace('.', ',')
        if ',' in new and len(new.split(',')[-1]) == 2:
            new = '.'.join(new.rsplit(',', 1))
        text = text.replace(old, new)
    return text
