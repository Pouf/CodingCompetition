# You must determine whether a given expression has valid brackets. This means
# all the parentheses (), square brackets [] and curly brackets {} must be
# correctly paired & nested.

# The expression does not contain whitespace characters.


e = ''.join(c for c in input() if c in '()[]{}')
pairs = ('{}', '[]', '()')
while any(pair in e for pair in pairs):
    for pair in pairs:
        e = e.replace(pair, '')

print(str(not e).lower())