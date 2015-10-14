def checkio(wordSet):
    return any(any(j.endswith(i) for i in wordSet if i != j) for j in wordSet)
