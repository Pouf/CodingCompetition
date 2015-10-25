FIRST_TEN = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def checkio(n):
    n1000 = n // 1000
    n100 = (n // 100) % 10
    n10 = (n // 10) % 10
    n1 = n % (10 if n10 > 1 else 20)
    t = FIRST_TEN[n1000-1] + 'thousand' if n1000 > 0 else ''
    t += FIRST_TEN[n100-1] + 'hundred' if n100 > 0 else '' 
    t += 'and' if (n1000 or n100) and (n10 or n1) else '' 
    t += OTHER_TENS[n10-2] if n10 > 1 else ''
    t += (FIRST_TEN+SECOND_TEN)[n1-1] if n1 > 0 else '' 
    return len(t)
