def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = [i for i in args[0]]
    mini = args[0]
    for i in args:
        if key:
            if key(i) < key(mini):
                mini = i
        else:
            if i < mini:
                mini = i
    return mini


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = [i for i in args[0]]
    maxi = args[0]
    for i in args:
        if key:
            if key(i) > key(maxi):
                maxi = i
        else:
            if i > maxi:
                maxi = i
    return maxi
