from re import findall
def checkio(maze_map):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dirmap = {'01':"E",'10':"S", '0x': "W", 'x0': "N"}
    paths = ['11']
    
    while paths:
        for each in list(paths):
            paths.remove(each)
            for dir in directions:
                tryPos = hex(int(each[-2:][0],16)+dir[0])[2]+hex(int(each[-2:][1],16)+dir[1])[2]
                # reaching the exit, add the last coords, convert to moves
                if tryPos == 'aa' :
                    i = each
                    each += tryPos
                    for coord in range(2,len(each)):
                        each = ''.join([each[:coord], hex(int(each[coord],16)-int(i[coord-2],16))[2], each[coord+1:]])
                    return ''.join([dirmap[d] for d in findall('..',each[2:])])
                # only add path to queue if it is not a wall and no other path has been here before
                if not maze_map[int(tryPos[0],16)][int(tryPos[1],16)] and not tryPos in findall('..',''.join(paths)):
                    paths.append(each + tryPos)
