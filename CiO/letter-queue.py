def letter_queue(commands):
    queue = []
    for command in commands:
        if command == 'POP':
            queue = queue[1:] or []
        else:
            queue += [command[-1]]
    return ''.join(queue)
