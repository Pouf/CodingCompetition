# A palindrome is a sequence of letters which reads the same backward as
# forward, like “madam” for example.
# For a given input string S, you have to return the longest palindrome found
# within. If multiple substrings qualify, print them all in the same order as
# they appear in S.


text = input()
result = []

data = "|%s|" % ("|".join(text))
right, center = 0, 0
m, n = 0, 0
d_len = len(data)
length = [0] * d_len

for i in range(d_len):
    len_i = max(1, min(length[2 * center - i], right - i))
    while i >= len_i < d_len - i and data[i - len_i] == data[i + len_i]:
        len_i += 1
    if right < len_i + i:
        right = len_i + i
        center = i
        if right - center >= n - m:
            m, n = center, right
            result.append(''.join([x for i, x in enumerate(data[2 * m - n + 1:n]) if i % 2]))
    length[i] = len_i

best = max(length) - 1
for r in result:
    if len(r) == best:
        print(r)
