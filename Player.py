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
        while (numSticks<1) or (numSticks>3): numSticks = int(input(f"How many sticks do you wish to nim? (1-{min(state[pileChoice-1],3)})\t").strip())

        newstate = state[:pileChoice-1] + ([(state[pileChoice-1]-numSticks)]*int((state[pileChoice-1]-numSticks)>0)) + state[pileChoice:]

        return newstate
    
class MinMaxPlayer(Player):
    def __init__(self,name):
        Player.__init__(self)
        self.name=name
        pass

    def turn(self,state):
        
        return state
        pass
    
    pass

    def min(self):
        pass

    def max(self):
        pass



class MCTSPlayer(Player):
    def __init__(self,name):
        Player.__init__(self)
        self.name=name
        pass
    
    pass