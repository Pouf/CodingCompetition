from sys import exit
from os.path import isfile
import queue
import threading
# from blist import blist


exitFlag = 0

'''
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()

threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", 
              "Thread-6", "Thread-7", "Thread-8"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue()
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
'''


# solve(1, ['hello world'])
# q = queue.Queue()

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
    solutions = []
    for i, block in enumerate(splitTask):
        # print(i+1, block)
        # t = threading.Thread(target=solve, args=(i+1, block))
        # t.daemon = True
        # t.start()
        n, solution = modules.solve(i+1, block)
        solutions.append('Case #{}: {}'.format(n, solution))
        # try to add to a blist then write to file
    # outFile = open(outFilePath, 'w')
    # outFile.write(solutions)
    # outFile.close()
    with open(outFilePath, 'w') as outFile:
        outFile.write('\n'.join(solutions))
    print('Done - {} cases'.format(n))


def main():
    root = 'D:/Dropbox/Google Code Jam/Africa2010/'
    files, options, execType = [], '', {}
    for P in ['a', 'b', 'c', 'd', 'e', 'f']:
        if isfile('{}{}.py'.format(root, P.upper())):
            files += [P]
    # P = input(', '.join(files)).upper()
    P = 'D'
    for T in ['test', 'small', 'large']:
        inFilePath = '{}{}-{}-practice.in'.format(root, P, T)
        if isfile(inFilePath):
            options += '{0[0]}: {0}\n'.format(T)
            execType[T[0]] = T

    # T = input(options)
    T = 'l'

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
