def checkio(chips):
    firstChip = chips[0]

    # assign a number to each chip
    chips = list(enumerate(chips))

    # set a minimum score of 0
    scores = [0]
    for x in range(3):
        tries = [['0', firstChip[x], 0]]
        while tries:
            t = tries.pop()
            remainingChips = [c for c in chips if str(c[0]) not in t[0]]
            for chip in remainingChips:
                chipValues = chip[1]
                for y, chipVal in enumerate(chipValues):
                    if t[1] == chipVal:
                        for z in [.5, -.5]:
                            next = chipValues[int(y-1.5+z)]
                            newScore = t[2] + chipValues[int(y-1.5-z)]
                            tries += [[t[0] + str(chip[0]), next, newScore]]
                            if len(remainingChips) == 1:
                                if next == firstChip[x-2]:
                                    scores += [newScore + firstChip[x-1]]
                                elif next == firstChip[x-1]:
                                    scores += [newScore + firstChip[x-2]]

    return max(scores)
