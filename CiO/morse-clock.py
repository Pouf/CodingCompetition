checkio=lambda t:' : '.join(' '.join(''.join('.-'[int(x)]for x in bin(int(d))[2:].zfill(int('243434'[i+2*j])))for i,d in enumerate(n.zfill(2)))for j,n in enumerate(t.split(':')))
