

def main(data):
    result = 0
    for line in data:
        batteries = list(line)
        best = max(batteries[:-1]
        position = batteries.index(best)
        remaining = vatteries[position:]
        next_best = max(remaining)
        result += int(f"{best}{next_best}")
    yield result