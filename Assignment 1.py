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
    
if __name__=="__main__":

    testCases=["MI","MIU","MUI","MIIII","MUUII","MUUUI"]

    print("MIU Tester Testing =w=\n")
    for case in testCases:
        print(case + ":\t" + str(nextStates(case)))
