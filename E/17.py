# Problem 17 - Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage.
FIRST_TEN = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
SECOND_TEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
OTHER_TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def n2words(number):
    n1000 = number // 1000
    n100 = (number // 100) % 10
    n10 = (number // 10) % 10
    n1 = number % (10 if n10 > 1 else 20)
    t = FIRST_TEN[n1000-1] + 'thousand' if n1000 > 0 else ''
    t += FIRST_TEN[n100-1] + 'hundred' if n100 > 0 else '' 
    t += 'and' if (n1000 or n100) and (n10 or n1) else '' 
    t += OTHER_TENS[n10-2] if n10 > 1 else ''
    t += (FIRST_TEN+SECOND_TEN)[n1-1] if n1 > 0 else '' 
    return len(t)
print(sum(map(n2words, range(1, 1001))))
