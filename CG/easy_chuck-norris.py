# Here is the encoding principle:

# The input message consists of ASCII characters (7-bit)
# The encoded output message consists of blocks of 0
# A block is separated from another block by a space
# Two consecutive blocks are used to produce a series of same value bits (only
# 1 or 0 values):
# - First block: it is always 0 or 00. If it is 0, then the series contains 1,
#   if not, it contains 0
# - Second block: the number of 0 in this block is the number of bits in the
#   series


message = [int(l) for x in input() for l in format(ord(x), '07b')]

result = ''
prev = 2
for c in message:
    if c == prev:
        result += '0'
    else:
        result += ' {} 0'.format(['00', '0'][bool(c)])
    prev = c
        
print(result.strip())