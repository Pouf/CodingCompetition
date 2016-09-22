def draw(segments):
    segments = sorted([s[:2], s[2:]] for s in segments)
    points = sum(segments, [])
    oddPoints = [p for p in set(points) if points.count(p)%2]
    if len(oddPoints) > 2:
        return []
    result = (oddPoints or points)[0]
    queue, paths = [[result]], []
    while queue:
        result = queue.pop()
        path = paths.pop() if paths else []
        if sorted(path) == segments:
            return result
        for v in segments:
            if v not in path and result[-1] in v:
                queue.append(result + [p for p in v if p != result[-1]])
                paths.append(path + [v])
    return []
