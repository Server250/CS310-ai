import time

# Part A
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

# Part B
def extendPath(p):
    retStates=[]
    for i in nextStates(p[-1]):
        retStates.append(p+[i])
    return retStates

# Part C
def breadthFirstSearch(goal):
    highestAgendaSize = 1 # Variable to track highest agenda size
    
    searchDepthLimit = 30 # Limit the depth of the search in case of impossible goal
    searchDepthCounter = 0 # Count up to the depth limit
    
    agenda =[["MI"]] # Initialise the agenda
    depthLimit = 1 # Number of elements to traverse before a layer is complete
    depthCount = 0 # Number of elements counted towards depthLimit
    extendCalls = 0

    while (searchDepthCounter<searchDepthLimit):
        #print("AGENDA IS " + str(agenda))
        depthCount+=1
        if depthCount==depthLimit:
            depthCount=0
            depthLimit*=2
            searchDepthCounter+=1
        
        currentPath = agenda.pop(0) # Retrieve first item from the queue
        if (currentPath[-1]==goal):
            print("BFS:\tMatch for " + goal + " found! Final length of the path was " + str(len(currentPath)) + ", and \"extendPaths\" was called " + str(extendCalls) + " times.")
            print("BFS:\tThe peak size of the agenda was " + str(highestAgendaSize) + ".")
            return currentPath
        else:
            agenda+=extendPath(currentPath)# Add new levels of the tree to the agenda
            extendCalls+=1
            if (len(agenda)>highestAgendaSize): highestAgendaSize=len(agenda)
            
    print("BFS:\tNo match found within the bounds of the search (depth limit of " + str(searchDepthLimit) +").")
    return -1

# Part D
def depthLimitedDFS(goal,limit):
    searchDepthLimit = 30 # Limit the depth of the search in case of impossible goal
    searchDepthCounter = 0 # Count up to the depth limit
    
    agenda =[["MI"]] # Initialise the agenda
    depthCounter = 1 # Count until the next layer of the tree is reached

    maxAgenda=1
    expandCalls=0

    while (len(agenda)>0):
        currentPath = agenda.pop(0) # Retrieve first item from the queue
        if (currentPath[-1]==goal):
            #print("Match for " + goal + " found! " + str(currentPath))
            return {"path":currentPath,"maxAgenda":maxAgenda,"expandCalls":expandCalls}
        else:
            searchDepthCounter+=1 # Add one to the depth counter
            if (len(currentPath)<limit):
                agenda=extendPath(currentPath)+agenda # Add new levels of the tree to the front of the agenda if length hasn't reached the limit
                expandCalls+=1
            
            if (len(agenda)>maxAgenda): maxAgenda=len(agenda) # Update maximum size of the agenda
            
    return None

def dfsIter(goal):
    givenLimit=2
    totalExpands=0
    maxAgenda=1

    finalPath=[]
    
    while True:
        res=depthLimitedDFS(goal,givenLimit)
        if (res):
            totalExpands+=res["expandCalls"]
            if (res["maxAgenda"]>maxAgenda): maxAgenda=res["maxAgenda"]
            finalPath=res["path"]
            break
        givenLimit+=1

    print ("DFS:\tMatch for " + goal + " found! The final length of the path was " + str(len(finalPath)) + " and \"expandPaths\" was called " + str(totalExpands) + " times.")
    print ("DFS:\tThe peak size of the agenda was " + str(maxAgenda) + ".")
    return finalPath
    
if __name__=="__main__":
    print("Exercise Two is running.")
    goalVal=input("Input a target MIU string:\t")
    print("\n")
    bfsTimer=time.perf_counter()
    print(breadthFirstSearch(goalVal))
    bfsTimer=abs(bfsTimer-time.perf_counter())
    print("\n")
    dfsTimer=time.perf_counter()
    print(dfsIter(goalVal))
    dfsTimer=abs(dfsTimer-time.perf_counter())
	
    print("\nThe breadth first search took " + str(bfsTimer) + "s to complete successfully.")
    print("The depth first search took " + str(dfsTimer) + "s to complete successfully.")

