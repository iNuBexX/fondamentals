class hanoi:
#define the initial peg 
    def __init__(self,init=1,target=2,N=10):  
        self.init=init#arbitrary peg 
        self.target=target
        self.disks=[n for n in range(N)][::-1]
        self.pegs ={1:[],2:[],3:[]}
        self.pegs[init].extend(self.disks)
        self.count=0
        self.N=N
        self.aux=6-target - init
    def SolveIter(self):
        lastMoved=0
        iter =0
        while(len(self.pegs[self.target])<len(self.disks)):
    
            
            for i in range(1,4):
                if i == lastMoved:
                    continue
                else:
                    if len(self.pegs[i])>0:
                        if (len(self.pegs[i])-1)%2==1 :#moving disk to a non target peg
                            if i==self.target:#the disk in question is in the target  (its target becomes the auxiliary)
                                if (len(self.pegs[self.init])<1) or int(self.pegs[self.init][-1]) > int(self.pegs[i][-1]):
                                    self.pegs[self.init].append(self.pegs[i].pop())#moving from target to init   -non target (non auxiliary)-
                                    lastMoved=self.init
                                    break
            
                            elif i ==self.aux:#the disk is on auxilary
                                if (len(self.pegs[self.init])<1) or self.pegs[self.init][-1] > self.pegs[i][-1]:
                                    self.pegs[self.init].append(self.pegs[i].pop())#moving from aux to init
                                    lastMoved=self.init
                                    break
                            else:
                                if (len(self.pegs[self.aux])<1) or self.pegs[self.aux][-1] > self.pegs[i][-1]:#disk on init
                                    self.pegs[self.aux].append(self.pegs[i].pop())#moving to non target 
                                    lastMoved=self.aux
                                    break

                        else: #moving disk to target peg
                            if i==self.target:#the disk in question is in the target  (its target becomes the auxiliary)
                                if (len(self.pegs[self.aux])<1) or self.pegs[self.aux][-1] > self.pegs[i][-1]:
                                    self.pegs[self.aux].append(self.pegs[i].pop())
                                    lastMoved=self.aux
                                    break
                            else:#the disk is on init
                                if  (len(self.pegs[self.target])<1) or len(self.pegs[self.target])<1 or (self.pegs[self.target][-1] > self.pegs[i][-1]):
                                    self.pegs[self.target].append(self.pegs[i].pop())#moving to non target
                                    lastMoved=self.target
                                    break
                    
                                
            
                pass

            pass
            



        pass
    def printTarget(self):
        print(self.pegs[self.target])
    def printInit(self):
        print(self.pegs[self.init])
            


puzzle = hanoi(1,2,9)#first example is the initial peg


#puzzle.printInit()
puzzle.SolveIter()
puzzle.printInit()
puzzle.printTarget()

#print(puzzle.count)

#print(puzzle.pegs[1][-1])
