import pandas as pd

nfa = {}

# TODO add parsing from a file
# with open("input.txt", "r") as inputFile:

states = int(input("Nr of states : "))
terminals = int(input("Nr of terminals : "))  #
for i in range(states):
    state = input("state name : ")
    nfa[state] = {}
    for j in range(terminals):
        path = input("path : ")
        print("Enter destination state from state {} through path {} : ".format(state, path))
        reachingState = [x for x in input().split()]
        nfa[state][path] = reachingState

print("NFA:")
print(nfa)
print("NFA table:")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("\nF= ")
nfaFinalState = [x for x in input().split()]

newStatesList = []
dfa = {}
keysList = list(list(nfa.keys())[0])
pathList = list(nfa[keysList[0]].keys())

dfa[keysList[0]] = {}
for i in range(terminals):
    var = "".join(nfa[keysList[0]][pathList[i]])
    dfa[keysList[0]][pathList[i]] = var
    if var not in keysList:
        newStatesList.append(var)
        keysList.append(var)

while len(newStatesList) != 0:

    dfa[newStatesList[0]] = {}

    for _ in range(len(newStatesList[0])):
        for i in range(len(pathList)):
            temp = []
            for j in range(len(newStatesList[0])):
                temp += nfa[newStatesList[0][j]][pathList[i]]
            s = ""
            s = s.join(temp)
            if s not in keysList:
                newStatesList.append(s)
                keysList.append(s)
            dfa[newStatesList[0]][pathList[i]] = s

    newStatesList.remove(newStatesList[0])

print("\nDFA:")
print(dfa)
print("DFA table :")
dfaTable = pd.DataFrame(dfa)
print(dfaTable.transpose())

dfaStatesList = list(dfa.keys())
dfaFinalStates = []
for x in dfaStatesList:
    for i in x:
        if i in nfaFinalState:
            dfaFinalStates.append(x)
            break

print("Final states of the DFA are : ", dfaFinalStates)
