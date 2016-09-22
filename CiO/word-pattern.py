from re import sub


def check_command(p, c):
  A = sub('\D','1', sub('\d','0',c))
  B = '{:0{}b}'.format(p, len(c))
  return A == B
