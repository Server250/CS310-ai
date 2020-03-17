import random
from Player import HumanPlayer
from Player import MinMaxPlayer
from Player import MCTSPlayer

def nim_game():
    # Setup stage
    gamePlaying = True
    gameState = []
    numPiles = -1
    maxPileSize = -1
    players=[]
    currentTurn = -1

    while numPiles<1: numPiles = int(input("How many piles?\t").strip())
    while maxPileSize<1: maxPileSize = int(input("Maximum pile size?\t").strip())

    for i in range(2):
        while (len(players)<i+1):
            ptype = input(f"What type should player {len(players)+1} be? (1 = Human | 2 = MiniMax | 3 = MonteCarlo)\t")

            if (int(ptype)==1):
                players.append(HumanPlayer(f"Player ({len(players)+1})"))
            elif (int(ptype)==2):
                players.append(MinMaxPlayer(f"Player ({len(players)+1})"))
            elif (int(ptype)==3):
                players.append(MCTSPlayer(f"Player ({len(players)+1})"))
            else:
                continue

    while currentTurn>1 or currentTurn<0: currentTurn = int(input("Which player should go first? (1 | 2)\t").strip())-1
   
    for _ in range(numPiles):
        random.seed()
        gameState.insert(0,random.randint(1,maxPileSize))

    print(f"The initial game state is: {gameState}.")
    c=2
    while (c>0) and (gamePlaying) and (gameState!=[]):

        

        print(f"\nThe current game state is: {gameState}. It is {players[currentTurn].name}'s turn!")

        if (type(gameState) != type([])):
            gameState=eval(gameState)

        gameState = players[currentTurn].turn(gameState)

        #c-=1
        currentTurn=int(not(bool(currentTurn))) # Change turn

    print(f"\nPlayer {int(not(bool(currentTurn))) + 1} Won!\nThe final game state is: {gameState}.\n")

if __name__=="__main__":
    print("Assignment 6 started.\n")
    nim_game()