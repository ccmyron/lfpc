import pandas as pd
import re

if __name__ == "__main__":

    nfa = {}

    with open("input.txt", "r") as inputFile:
        lines = inputFile.readlines()
    inputFile.close()

    entries = len(lines)

    # parse all the states
    states = int(lines[0].rstrip(',\n'))

    # parse a list with all the paths
    terminalsLine = lines[1]
    terminalsLine = filter(lambda c: c not in " ,\n", terminalsLine)
    terminalList = [x for x in terminalsLine]

    i = 2
    while i < entries-1:

        fileLine = lines[i].split('=')

        state = "".join(fileLine[0]).split(',')[0]

        # initialize empty list for each path
        if state not in nfa:  
            nfa[state] = {x: [] for x in terminalList}

        # parse the terminal symbol
        path = fileLine[0][-1]  

        # parse the state we reach through this path
        reachingState = fileLine[1][0]  
        if reachingState not in nfa[state][path]:
            nfa[state][path].append(reachingState)

        i += 1

    # parse the final states
    finalStatesLine = lines[entries-1]
    nfaFinalStatesList = re.search(r"{(.*)}", finalStatesLine).group(1).split(',')

    print("\nNFA table:")
    nfa_table = pd.DataFrame(nfa)
    print(nfa_table.transpose())
    

    # write out the first line: state and the states we reach through all paths
    dfa = {}
    newStatesList = []
    keysList = [list(nfa.keys())[0]]
    dfa[keysList[0]] = {}
    for i in range(len(terminalList)):
        tempPath = "".join(nfa[keysList[0]][terminalList[i]])
        dfa[keysList[0]][terminalList[i]] = tempPath
        if len(tempPath) > 0 and tempPath not in keysList:
            newStatesList.append(tempPath)
            keysList.append(tempPath)


    #  if a new state appears, add it to the DFA, and go through the states using all paths
    # until we find all possible permutations of the states.\
    while len(newStatesList) != 0:

        dfa[newStatesList[0]] = {}

        for _ in range(len(newStatesList[0])):
            for i in range(len(terminalList)):
                temp = []
                for j in range(len(newStatesList[0])):
                    temp += nfa[newStatesList[0][j]][terminalList[i]]
                dfaState = ""
                dfaState = dfaState.join(temp)
                if len(dfaState) > 0 and dfaState not in keysList:
                    newStatesList.append(dfaState)
                    keysList.append(dfaState)
                dfa[newStatesList[0]][terminalList[i]] = dfaState

        newStatesList.remove(newStatesList[0])

    print("\nDFA table:")
    dfaTable = pd.DataFrame(dfa)
    print(dfaTable.transpose())


    # find the final states of the DFA
    dfaStatesList = list(dfa.keys())
    dfaFinalStates = []
    for x in dfaStatesList:
        for i in x:
            if i in nfaFinalStatesList:
                dfaFinalStates.append(x)
                break

    print("Final states of this DFA are:", dfaFinalStates)
