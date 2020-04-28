import random as rand
import networkx as nx
import matplotlib.pyplot as plt

NB_NODE_MAX=40
CENTRALISATION_MAX=(NB_NODE_MAX/2)
NB_LONG_MAX=100

def init():
    G=nx.Graph()
    for x in range(NB_NODE_MAX):
        G.add_edge(rand.randrange(0, CENTRALISATION_MAX), rand.randrange(0, CENTRALISATION_MAX), longueur=rand.randrange(0, NB_LONG_MAX))
    #print(G.edges.data())
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

if __name__ == "__main__":
    init()
