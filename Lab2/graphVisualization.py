import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import re
import random
from networkx.drawing.nx_agraph import write_dot

if __name__ == "__main__":
    # dfa = {
    #     '0': {
    #         'a': '0',
    #         'b': '1',
    #         'c': ''
    #         },
    #     '1': {
    #         'a': '1',
    #         'b': '',
    #         'c': '12'
    #         },
    #     '12': {
    #         'a': '10',
    #         'b': '',
    #         'c': '12'
    #         },
    #     '10': {
    #         'a': '10',
    #         'b': '1',
    #         'c': '12'
    #         }
    # }

    dfa = {
        '0': {
            'a': '0',
            'b': '1',
        },
        '1': {
            'a': '',
            'b': '',
        }
    }

    pathList = ['a', 'b', 'c']
    dfaGraph = nx.MultiDiGraph()
    states = list(dfa.keys())
    numberOfStates = len(states)

    positionsX = random.sample(range(1, 6), len(states))
    positionsY = random.sample(range(1, 6), len(states))

    for i in range(numberOfStates):
        dfaGraph.add_node(states[i], pos=(positionsX[i], positionsY[i]))

    for i in range(numberOfStates):
        for j in range(len(dfa[states[i]])):
            destination = dfa[states[i]][pathList[j]]
            if len(destination) > 0:

                dfaGraph.add_edge(states[i], destination, path=pathList[j])

    nx.nx_agraph.write_dot(dfaGraph, 'multi.dot')

    # path = nx.get_edge_attributes(dfaGraph, 'path')
    # pos = nx.get_node_attributes(dfaGraph, 'pos')
    #
    # # draw this bullshit
    # plt.figure()
    # nx.draw_networkx(dfaGraph, pos)
    # nx.draw_networkx_edge_labels(dfaGraph, pos, edge_labels=path)
    # plt.show()

    # for i in range(len(dfa[states[1]])):
    #     if len(dfa[states[1]][pathList[i]]) > 0:
    #         print(pathList[i])
    #         print(dfa[states[1]][pathList[i]])
