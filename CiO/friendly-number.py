def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    power = 0
    while abs(number) >= base**(power + 1) and power < len(powers) - 1:
        power += 1
    number /= base**power
    if not decimals:
        number = int(number)

    result = '{0:.{1}f}{2}{3}'.format(number, decimals, powers[power], suffix)
    return result
