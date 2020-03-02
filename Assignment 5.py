# Return the minimax value of a game at position state
def minimax_value(state):

    if (bool(state[1]-1)):  # If player min's turn
        return min_move(state, -1*float("inf"), float("inf"))
    else:                   # If player max's turn
        return max_move(state, -1*float("inf"), float("inf"))

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

    return return_states

# Evaluate the game from the Min player's view
def min_move(state, a, b):
    val=float("inf") # The highest possible value is the default minimum
    alpha = a
    beta = b

    terminate = is_terminal(state)
    if (bool(terminate)): return terminate # If game has terminated, return the utility score
    
    for s in successor_moves(state): # For all possible successive states
        newScore = max_move(s, alpha, beta)
        
        if newScore<val:
            val = newScore
        if newScore<=alpha: # This alpha is passed down, so v best alternative from across the tree
            return val
        if newScore<beta:
            beta = newScore

        # Update the utility val of the min player
        """if newScore<val:
            val = newScore"""

    return val

# Evaluate the game from the Max player's view (ssf = state so far)
def max_move(state, a, b):
    val=-1*(float("inf")) # The lowest possible value is the default maximum
    alpha = a
    beta = b

    terminate = is_terminal(state)
    if (bool(terminate)): return terminate # If game has terminated, return the utility score
    
    for s in successor_moves(state): # For all possible successive states
        newScore = min_move(s, alpha, beta)
        
        if newScore>val:
            val = newScore
        if newScore>=beta: # This beta is passed down, so v best alternative from across the tree
            return val
        if newScore>alpha:
            alpha = newScore
        
        # Update the utility val of the max player
        """if newScore>val:
            val = newScore"""

    return val

def minvalue_prune(state, alpha, beta):
    print("minv")

def maxvalue_prune(state, alpha, beta):
    print("maxv")

if __name__=="__main__":
    print("Assignment 4 : NIM Player Started\n")

    tests = [([2,3],1),([5,5,5],1),([1,2],2)]
    test_results = [1,-1,-1]

    for i,t in enumerate(tests):
        tscore = minimax_value(t)
        #paths = {0:(max_path+[([],1)]),1:(min_path+[([],2)])}
        print(f"Test {i+1} is {t}. \tReturned value: {tscore}\tExpected value: {test_results[i]}")
        #print(f"Game path was: {paths[int(not (tscore>0))]}\n")
