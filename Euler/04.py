print(max(a*b for a in range(999, 100, -1) for b in range(999, 100, -1) if str(a*b)==str(a*b)[::-1]))
