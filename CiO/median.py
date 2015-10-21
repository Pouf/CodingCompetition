def checkio(data):
    sData, qty = sorted(data), len(data)
    mid, odd = qty//2, qty & 1
    return sum(sData[mid-1+odd:mid+1])/(2-odd)
