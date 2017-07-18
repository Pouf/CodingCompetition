# Your program must decode the encoded message from the Chuck Norris encoding
# project.

# It is strongly recommended to have done the Chuck Norris project.
# Link -> https://www.codingame.com/training/easy/chuck-norris


# Here are some reminders about the Chuck Norris encoding method:
# - The encoded message is unary, containing only sequences of zeroes separated
#   by spaces.
# - These sequences of zeroes always come in pairs.
# - The first sequence of a pair can be either 0 or 00, which represent the
#   binary bits 1 and 0 respectively.
# - The second sequence of a pair is made of k zeroes, where k is the number of
#   time the previous bit has to be printed in order to decode the message.

# For instance, if we want to encode the character A, we first start to write
# down the 7-bit ASCII code for A which is 1000001 in binary. (We only use 7
# bits because the first bit is always zero so it's ignored).
# Then we turn the binary into unary as follows:
# 1000001 -> 0 0 (bit 1, one time)
# 1000001 -> 00 00000 (bit 0, five times)
# 1000001 -> 0 0 (bit 1, one time)
# Therefore, the encoded message is 0 0 00 00000 0 0.


# You are asked to do the reverse process, and thus print A when given the
# message 0 0 00 00000 0 0.
# If the input is invalid, just print INVALID.


encrypt = input().split()
result = 'INVALID'
if not len(encrypt) % 2:
    encrypt = [encrypt[i:i+2] for i in range(0, len(encrypt), 2)]
    result = ''
    for k, v in encrypt:
        if k == '0':
            result += '1' * len(v)
        elif k == '00':
            result += '0' * len(v)
        else:
            break
    if len(result) % 7 or not result:
        result = 'INVALID'
    else:
        result = [chr(int(result[i:i+7], 2)) for i in range(0, len(result), 7)]
print(*result, sep='')