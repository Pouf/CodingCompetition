import re
def flat_list(a):
    return [int(i) for i in re.findall('-?\d+',`a`)]
