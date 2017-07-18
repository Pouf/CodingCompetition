def digit_stack(commands):
    result, stack = [], []

    for c in commands:
        c, *n = c.split()
        stack += n
        if not n:
            result += stack[-1:]
            if 'O' in c:
                try: stack.pop()
                except IndexError: pass

    return sum(map(int, result))
