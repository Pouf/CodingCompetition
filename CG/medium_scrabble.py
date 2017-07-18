# Your objective is to find the word that scores the most points using the
# available letters (1 to 7 letters).
# A dictionary of authorized words is provided as input for the program. The
# program must find the word in the dictionary which wins the most points for
# the seven given letters (a letter can only be used once). If two words win
# the same number of points, then the word which appears first in the order of
# the given dictionary should be chosen.

# All words will only be composed of alphabetical characters in lower case.
# There will always be at least one possible word.
  

from collections import Counter


TABLE = str.maketrans('eaionrtlsudgbcmpfhvwykjxqz',
                      '111111111122333344444588AA')
n = int(input())
words = [input() for _ in range(n)]
letters = Counter(input())

word, top = [], 0
for w in words:
    if not Counter(w) - letters:
        points = sum(int(l, base=16) for l in w.translate(TABLE))
        if points > top:
            top = points
            word = w
print(word)