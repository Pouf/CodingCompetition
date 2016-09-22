def checkio(teleports_string):
    queue, paths = ['1'], []
    while queue:
        result = queue.pop()
        path = paths.pop() if paths else []
        if set('12345678') <= set(result) and result[-1] == '1':
            return result
        for v in teleports_string.split(','):
            if v not in path and result[-1] in v:
                queue.append(result + v[v[1]!=result[-1]])
                paths.append(path + [v])
