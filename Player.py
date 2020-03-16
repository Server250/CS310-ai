import random

class Player():
    def __init__(self):
        pass

    def turn(self,state):
        return state

    pass

class HumanPlayer(Player):
    def __init__(self,name):
        Player.__init__(self)
        self.name=name
        pass

    def turn(self,state):
        pileChoice = -1
        numSticks = -1

        while (pileChoice<1) or (pileChoice>len(state)): pileChoice = int(input(f"Which pile would you like to nim from? (1-{len(state)})\t").strip())
        while (numSticks<1) or (numSticks>min(state[pileChoice-1],3)): numSticks = int(input(f"How many sticks do you wish to nim? (1-{min(state[pileChoice-1],3)})\t").strip())

        newstate = state[:pileChoice-1] + ([(state[pileChoice-1]-numSticks)]*int((state[pileChoice-1]-numSticks)>0)) + state[pileChoice:]

        return newstate
    
class MinMaxPlayer(Player):
    def __init__(self,name):
        Player.__init__(self)
        self.name=name
        self.relations={}
        self.goalState=[]
        pass

    def turn(self,state):
        
        #print(f"{self.succStates(state)}")

        # Clear relations
        self.relations.clear()

        if (self.min(state, -1*float("inf"), float("inf")) < 0):
            return (self.buildPath(self.goalState)[1])
        else:
            print("No good one found, shit fizucked")
            retState = state
            randPile = random.randint(0,len(retState)-1)
            retState[randPile]-=random.randint(1,retState[randPile])
            
            retState=[x for x in retState if x != 0]
            
            return retState
        
    def min(self, state, a, b):
        val=float("inf") # The highest possible value is the default minimum
        alpha = a
        beta = b

        if (state==[]):
            self.goalState=state
            return -1

        for s in self.succStates(state): # For all possible successive states
            self.relations[repr(s)]=repr(state)
            newScore = self.max(s, alpha, beta)
            
            if newScore<val:
                val = newScore
            if newScore<=alpha: # This alpha is passed down, so v best alternative from across the tree ALPHA PRUNING
                return val
            if newScore<beta:
                beta = newScore

        return val
        
    def max(self, state, a, b):
        val=-1*float("inf") # The highest possible value is the default minimum
        alpha = a
        beta = b

        if (state==[]):
            return 1

        for s in self.succStates(state): # For all possible successive states
            self.relations[repr(s)]=repr(state)
            newScore = self.min(s, alpha, beta)
            
            if newScore>val:
                val = newScore
            if newScore>=beta: # This beta is passed down, so v best alternative from across the tree BETA PRUNING
                return val
            if newScore>alpha:
                alpha = newScore

        return val

    def succStates(self,state):
        return_states=list()

        for i, pile in enumerate(state): # For every remaining pile
            for n in range(1,3+1):
                if pile>=n: return_states.append([]+state[:i]+([(pile-n)]*int((pile-n)>0))+state[i+1:])

        return return_states

    def buildPath(self,state):
        retPath = []
        s = repr(state)
        while (not self.relations[s] == ""):
            retPath.insert(0,self.relations[s])
            s=self.relations[s]

class MCTSPlayer(Player):
    def __init__(self,name):
        Player.__init__(self)
        self.name=name
        pass
    
    pass