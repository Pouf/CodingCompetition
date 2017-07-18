# You must print the greatest number using all the characters in the input,
# including the ten digits 0 to 9, the minus sign - and the decimal dot ..

# Beware:
# * The dot alone must not end a number, at least a digit is needed. For
# example, 98742. is refused, write 9874.2 instead.
# * Trailing and leading zeros must be removed. Write -4 instead of -4.0000 and
# -5.65 instead of-5.6500.
 

input()
n = input().split()
negative = '-' in n

result = sorted([i for i in n if i.isdigit()], reverse=not negative)

if negative:
    result.insert(0, '-')
if '.' in n:
    result.insert(2 if negative else -1, '.')

result = ''.join(result).strip('0').strip('.')

if not float(result):
    result = '0'

print(result)