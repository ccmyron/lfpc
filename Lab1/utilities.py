# library for all the functions
# solely for readability purposes

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import re as reeeeeeeeeeeeeee

graph = defaultdict(list)

def addEdge(graph,u,v): 
  graph[u].append(v) 
# end of addEdge function

def parseString(str):

  str = str.split()
  str = "".join(str).split("P={")[1]
  if str[-1] == '}':
      str = str[:-1]
  str = reeeeeeeeeeeeeee.split("\d+\.", str)
  return list(filter(len, str))
# end of parseString function

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
# end of checkAutomaton function

def addToGraph(list):

  for i in list:
    temp = i.split("->")
    currentGraph =temp[0]
    pointTo = temp[1]
    if len(pointTo) < 2:
      addEdge(graph, currentGraph, {'None': pointTo[0]})
    else:
      addEdge(graph, currentGraph, {pointTo[1]: pointTo[0]})
# end of addToGraph function

def draw():  

  g = nx.DiGraph()
  for k, v in graph.items():
    for vv in v:
      for t in vv:
        g.add_edge(k,t) 
  nx.draw(g,with_labels=True)
  plt.draw()
  plt.show()
# end of draw function
