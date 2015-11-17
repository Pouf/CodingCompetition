def count_neighbours(g,r,c):
  h = range(max(r-1,0),min(r+2,len(g)))
  v = range(max(c-1,0),min(c+2,len(g[0])))
  neighbours = sum(g[x][y]for x in h for y in v) - 1
  return neighbours
