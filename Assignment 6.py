import random

def nim_game():
    # Setup stage
    gamePlaying = False
    gameState = []
    numPiles = -1
    maxPileSize = -1
    playerTurn = -1

    while numPiles<1: numPiles = int(input("How many piles?\t").strip())
    while maxPileSize<1: maxPileSize = int(input("Maximum pile size?\t").strip())
    while playerTurn>1 or playerTurn<0: playerTurn = int(input("Would you like to go first or second? (1 | 2)\t").strip())-1
    
    for _ in range(numPiles):
        random.seed()
        gameState.insert(0,random.randint(1,maxPileSize))

    print(f"The initial game state is: {gameState}")

    while gamePlaying:
        gamePlaying = False

if __name__=="__main__":
    print("Assignment 6 started.")
    nim_game()