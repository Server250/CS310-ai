import random
from Assignment6CPU import player

def nim_game():
    # Setup stage
    gamePlaying = True
    gameState = []
    numPiles = -1
    maxPileSize = -1
    playerTurn = -1
    turnNames = {}
    currentTurn = 0

    while numPiles<1: numPiles = int(input("How many piles?\t").strip())
    while maxPileSize<1: maxPileSize = int(input("Maximum pile size?\t").strip())
    while playerTurn>1 or playerTurn<0: playerTurn = int(input("Would you like to go first or second? (1 | 2)\t").strip())-1
    turnNames[playerTurn] = "your"
    turnNames[int(not(bool(playerTurn)))] = "the computer's"
   
    for _ in range(numPiles):
        random.seed()
        gameState.insert(0,random.randint(1,maxPileSize))

    #print(f"The initial game state is: {gameState}.")
    c = 5 # Debug value, allow c turns
    while gamePlaying:

        print(f"\nThe current game state is: {gameState}. It is {turnNames[currentTurn]} turn!")
        
        if currentTurn==playerTurn:
            gameState = human_turn(gameState)
        else:
            gameState = computer_turn(gameState)

        currentTurn=int(not(bool(currentTurn))) # Change turn
        
        c-=1
        if (c<=0):
            gamePlaying = False

def human_turn(state):
    pileChoice = -1
    numSticks = -1

    while (pileChoice<1) or (pileChoice>len(state)): pileChoice = int(input(f"Which pile would you like to nim from? (1-{len(state)})\t").strip())
    while (numSticks<1) or (numSticks>state[pileChoice-1]): numSticks = int(input(f"How many sticks do you wish to nim? (1-{state[pileChoice-1]})\t").strip())

    newstate = state[:pileChoice-1] + ([(state[pileChoice-1]-numSticks)]*int((state[pileChoice-1]-numSticks)>0)) + state[pileChoice:]

    return newstate

def computer_turn(state):

    return state

if __name__=="__main__":
    print("Assignment 6 started.")
    nim_game()