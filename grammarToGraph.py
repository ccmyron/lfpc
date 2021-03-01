from collections import defaultdict 
import networkx as nx
import matplotlib.pyplot as plt
import re as reeeeeeeeeeeeeee

graph = defaultdict(list)

def addEdge(graph,u,v): 
    graph[u].append(v) 
  
def parseString(str):
    str = str.split()
    str = "".join(str).split("P={")[1]
    if str[-1] == '}':
        str = str[:-1]
    str = reeeeeeeeeeeeeee.split("\d+\.", str)
    return list(filter(len, str))

def checkAutomaton(graph, source, word):
    for neighbour in graph[source]:
        for key in neighbour:
            if neighbour[key] == word[0]:
                word = word[1:]
                if len(word) == 0 and key == "None":
                    return True
                else:
                    if len(word) == 0 or key == "None":
                        return False
                return checkAutomaton(graph, key, word)
    return False

def addToGraph(list):
    for i in list:
        temp = i.split("->")
        currentGraph =temp[0]
        pointTo = temp[1]
        if len(pointTo) < 2:
            addEdge(graph, currentGraph, {'None': pointTo[0]})
        else:
            addEdge(graph, currentGraph, {pointTo[1]: pointTo[0]})

def draw():  
    g = nx.DiGraph()
    for k, v in graph.items():
        for vv in v:
            for t in vv:
                g.add_edge(k,t) 
    nx.draw(g,with_labels=True)
    plt.draw()
    plt.show()

if __name__ == "__main__":
    
    s = """VN={S, B, D},
        VT={a, b, c, d},
        P={
        1. S ->aS
        2. S ->bB
        3. B ->cB
        4. B ->d
        5. B ->aD
        6. D ->aB
        7. D ->b
        }"""
    while True:
        word = input("Type in a word to be checked:\n")
        addToGraph(parseString(s))
        print(checkAutomaton(graph, 'S', word))
        draw()
