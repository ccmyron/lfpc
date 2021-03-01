from collections import defaultdict 
from utilities import *

if __name__ == "__main__":
    graph = defaultdict(list)
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

