from sys import exit
from os.path import isfile
from blist import blist


def solveCodeJam(algo, inFilePath, outFilePath):
    print('Input : \'{}\'\nOutput : \'{}\''.format(inFilePath, outFilePath))

    inFile = open(inFilePath, 'r')
    d = inFile.read().splitlines()
    inFile.close()
    n, *d = d

    l = len(d)
    b = l//int(n)
    splitTask = (d[i:i+b] for i in range(0, l, b))

    modules = __import__(algo)
    solutions = blist([])
    for i, block in enumerate(splitTask):
        print(i+1, block)
        n, solution = modules.solve(i+1, block)
        solutions.append('Case #{}: {}'.format(n, solution))
    with open(outFilePath, 'w') as outFile:
        outFile.write('\n'.join(solutions))
    print('Done - {} cases'.format(n))


def main():
    root = 'D:/Dropbox/Google Code Jam/2015 Finals/'
    files, options, execType = [], '', {}
    for P in ['a', 'b', 'c', 'd', 'e', 'f']:
        if isfile('{}{}.py'.format(root, P.upper())):
            files += [P]
    # P = input(', '.join(files)).upper()
    P = 'C'
    for T in ['test', 'small', 'large']:
        inFilePath = '{}{}-{}-practice.in'.format(root, P, T)
        if isfile(inFilePath):
            options += '{0[0]}: {0}\n'.format(T)
            execType[T[0]] = T

    # T = input(options)
    T = 't'

    execType = execType.get(T, 'err')
    if execType == 'err':
        print('Wrong letter. Try again')
    else:
        if isfile('{}{}.py'.format(root, P)):
            inFilePath = '{}{}-{}-practice.in'.format(root, P, execType)
            outFilePath = '{}{}-{}-practice.out'.format(root, P, execType)
            solveCodeJam(P, inFilePath, outFilePath)
        else:
            print('can\'t find {}.py file in {}'.format(P, root))


if __name__ == '__main__':
    main()
