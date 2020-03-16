class Player():
    def __init__(self):
        pass

    def turn(self):
        pass

    pass

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.turnname="your"
        pass

    def turn(self,state):
        pileChoice = -1
        numSticks = -1

        while (pileChoice<1) or (pileChoice>len(state)): pileChoice = int(input(f"Which pile would you like to nim from? (1-{len(state)})\t").strip())
        while (numSticks<1) or (numSticks>state[pileChoice-1]): numSticks = int(input(f"How many sticks do you wish to nim? (1-{state[pileChoice-1]})\t").strip())

        newstate = state[:pileChoice-1] + ([(state[pileChoice-1]-numSticks)]*int((state[pileChoice-1]-numSticks)>0)) + state[pileChoice:]

        return newstate
    
    pass
    
class MinMaxPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.turnname="MinMax Computer's"
        pass
    
    pass

class MCTSPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.turnname="MCTS Computer's"
        pass
    
    pass