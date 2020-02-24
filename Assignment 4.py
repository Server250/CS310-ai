# Return the minimax value of a game at position state
def minimax_value(state):
    print(f"MMV CALLED WITH {state}")
    if (bool(state[1]-1)):  # If player min's turn
        return min_move(state)
    else:                   # If player max's turn
        return max_move(state)

# Return val if state is terminal, 0 if not
def is_terminal(state):
    if (state[0] == []) or (sum(state[0]) == 0):      # If there are no moves remaining
        if state[1] == 1:   # Win for Max
            return 1
        else:               # Win for Min
            return -1
    return 0

# Return successive moves from state state
def successor_moves(state):
    piles=state[0]
    next_player={1:2,2:1}[state[1]]
    return_states=list()

    for i, pile in enumerate(piles): # For every remaining pile
        for n in range(1,3+1):
            if pile>=n: return_states.append(tuple(([]+piles[:i]+([(pile-n)]*int((pile-n)>0))+piles[i+1:],next_player)))
    
    print(f"RETURN STATES: {return_states}")
    return return_states

# Remove duplicate states from a list of states
def removeDuplicates(states): # TODO list comprehension
    print("STUB")

# TODO Merge min and max move functions into one, tasty func
# Evaluate the game from the Min player's view
def min_move(state):
    val=1 # The highest possible value is the default minimum
    
    terminate = is_terminal(state)
    if (bool(terminate)): 
        print(f"TERMINATED {state}")
        return terminate # If game has terminated, return the utility score
    
    for s in successor_moves(state): # For all possible successive states
        val = min(val, max_move(s)) # Update the utility val of the min player

    return val

# Evaluate the game from the Max player's view
def max_move(state):
    val=-1 # The lowest possible value is the default maximum
    
    terminate = is_terminal(state)
    if (bool(terminate)): return terminate # If game has terminated, return the utility score
    
    for s in successor_moves(state): # For all possible successive states
        val = max(val, min_move(s)) # Update the utility val of the max player

    return val

if __name__=="__main__":
    print("Assignment 4 : NIM Player Started\n")

    tests = [([2,3],1),([5,5,5],1),([1,2],2)]
    test_results = [1,-1,-1]

    # piles=[2,1,1]
    # print(([]+piles[:1]+([(1-1)]*int((1-1)>0))+piles[1+1:],1))

    for i,t in enumerate(tests):
        print(f"Test {i+1} is {t}. Returned value: {minimax_value(t)}\tExpected value: {test_results[i]}")
