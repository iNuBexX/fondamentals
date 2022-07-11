class hanoi:
#define the initial peg 
    def __init__(self,init=1,target=2,N=10):  
        self.init=init=1#arbitrary peg 
        self.target=target
        self.disks=[n for n in range(N)]
        self.pegs ={1:[],2:[],3:[]}
        self.pegs[init].extend(self.disks)
        self.count=0
        self.N=N
        self.aux=6-target - init
    def SolveRec(self,disks,source,dest,aux):
        if  disks==1:
            self.pegs[dest].append(self.pegs[source].pop())
            self.count+=1

        else:
            self.SolveRec((disks-1),source,aux,dest)
            self.pegs[dest].append(self.pegs[source].pop())
            self.count+=1
            self.SolveRec((disks-1),aux,dest,source)

        pass
    def printTarget(self):
        print(self.pegs[self.target])
    def printInit(self):
        print(self.pegs[self.init])
            


puzzle = hanoi(1,2,4)#first example is the initial peg


puzzle.printInit()
puzzle.SolveRec(puzzle.N,puzzle.init,puzzle.target,puzzle.aux)

puzzle.printTarget()

print(puzzle.count)

