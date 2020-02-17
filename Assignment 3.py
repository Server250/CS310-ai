import time

def nextStates(s):
    returnStates = []
    
    # Rule 1
    if s[-1] == "I":
        returnStates.append(s+"U")

    # Rule 2
    if s[0]=="M":
        returnStates.append("M"+(s[1:]*2))
        
    # Rule 3
    tiIndex = s.find("III")
    throwAway=""
    while tiIndex>=0: # While there are IIIs
        returnStates.append(throwAway+s[:tiIndex]+"U"+s[len(throwAway)+tiIndex+3:]) # Add the new state to the return list
        throwAway= s[:len(throwAway)+2] # Update throwaway
        tiIndex=s[len(throwAway):].find("III") # Find more of them IIIs
            
    # Rule 4
    tiIndex = s.find("UU")
    throwAway=""
    while tiIndex>=0: # While there are UUUs
        returnStates.append(throwAway+s[:tiIndex]+s[len(throwAway)+tiIndex+2:]) # Add the new state to the return list
        throwAway= s[:len(throwAway)+1] # Update throwaway
        tiIndex=s[len(throwAway):].find("UU") # Find more of them IIIs

    return list(dict.fromkeys(returnStates)) # Remove duplicates

def extendPath(p):
    retStates=[]
    for i in nextStates(p):
        retStates.append(i)
    return retStates

def dictBFS(goal):
    nodes = {"MI":None} # Dictionary holding node(k) to parent(v) relations
    agenda = ["MI"]

    layerLimit = 30 # Limit the algorithm for no infinity
    curLayer = 1 # Track the current layer
    layerCount = {"currLayer":1,"nextLayer":0} # Count contents of layers, first val is number left in this layer, second val is size of next layer

    while (curLayer<layerLimit):
        
        currNode = agenda.pop(0) # Retrieve first element from agenda queue

        if currNode==goal:
            print("Match for \"" + goal + "\" found!")
            retPath=[currNode]
            # Construct final path for return
            nextParent=nodes[retPath[0]]
            while (nextParent): # While a parent exists for the most recently added node
                retPath.insert(0,nextParent)
                nextParent=nodes[retPath[0]]

            return retPath

        else:
            expandedPath=extendPath(currNode)
            for p in expandedPath:
                nodes[p]=currNode # Add the new nodes to the dictionary
            layerCount["nextLayer"]+=len(expandedPath) # Add the new nodes to the size of the next layer
            agenda+=expandedPath # Add the new nodes to the agenda for consideration

        layerCount["currLayer"]-=1 # Update layer counting, make sure tracked appropriately
        if layerCount["currLayer"]<=0:
            layerCount["currLayer"]=layerCount["nextLayer"]
            layerCount["nextLayer"]=0
            curLayer+=1        

    print("No match found for \"" + goal + "\" within the limits.")
    return None # No match found

# TODO Everything
# TODO Add comments for performance tracking
def estimateSteps(current,goal):
    return int(not (current==goal)) # placeholder stub

def aStarSearch(goal):
    agenda = ["MI"]
    visited = {} # Dictionary of visited nodes in form node:distanceFromStart
    found = (goal=="MI")
    
    #while not found:
        
        # get the lowest node A* score (distSoFar+expectedSteps) from the agenda 

        # If the node is the goal, yeet it as a treat
            # Say match is good
            # Construct return path
            # Return it ;P

        # Otherwise
            # get extendPaths for the current node
            # Add these with their distance from the start (current node's distance+1) to the agenda
            # Add the current node to visited with its A* score
    
    return "SHMARMP"

if __name__=="__main__":
    print("CS310 Ex3 Started.")
    
    #bfsTimer=time.perf_counter()
    print(dictBFS("MIUIU"))
    #print("This solution was found in " + str(bfsTimer-time.perf_counter()) + "s.\n")

    print("\n")

    print(aStarSearch("MI"))

