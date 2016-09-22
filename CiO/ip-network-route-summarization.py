def checkio(d):
    binIPs = [''.join('{0:08b}'.format(int(s)) for s in a.split('.')) for a in d]

    subnet = 32
    while len(set(i[:subnet] for i in binIPs)) > 1:
        subnet -= 1

    route = binIPs[0][:subnet].ljust(32, '0')
    route = '.'.join(str(int(route[i:][:8], 2)) for i in range(0, 32, 8))

    return '{0}/{1}'.format(route, subnet)
