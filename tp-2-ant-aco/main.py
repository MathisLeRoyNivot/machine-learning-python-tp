import random as rand
import networkx as nx
import matplotlib.pyplot as plt
from numpy.random import choice
import time
import numpy as np

NODE_MAX_QTY = 50
CENTRALISATION_MAX = (NODE_MAX_QTY / 2)
MAX_LENGTH_AMOUNT = 100

TRY_AMOUNT = 100
ANT_QTY = 100

# Start where all ants start from...
START_NODE = 0
# Finish node where the food is...
FINISH_NODE = 19

# Initialize Networkx Graph
G = nx.Graph()


def init():
    # Generate random edges based on random start and end node with random 'length'
    for x in range(NODE_MAX_QTY):
        G.add_edge(rand.randrange(0, CENTRALISATION_MAX), rand.randrange(
            0, CENTRALISATION_MAX), length=rand.randrange(0, MAX_LENGTH_AMOUNT), pheromone=1)


def launch():
    # Start timer
    start_time = time.time()
    for i in range(TRY_AMOUNT):
        for j in range(ANT_QTY):
            node = START_NODE
            visited_nodes = [START_NODE]
            while node != FINISH_NODE:
                node = choose_next_node(node, visited_nodes)
                if node == -1:
                    break
                visited_nodes.append(node)
            if node == FINISH_NODE:
                spread_pheromone(visited_nodes)
        evaporate_pheromone()
    get_shortest_path()
    # End timer & print resolve time
    print(f'Path found in {round(time.time() - start_time , 3)} seconds')
    plt.show()


def choose_next_node(node, visited_nodes):
    # G.degree gives the number of edges adjacent to the node
    some_length = G.degree(node, weight='length')
    # print(some_length)
    somme_pheromones = G.degree(node, weight='pheromone')
    # print(somme_pheromones)
    probs = []
    arrives = []

    if some_length == 0 or somme_pheromones == 0:
        return -1

    for node1, node2, data in G.edges(node, data=True):
        if visited_nodes.count(node2) <= 0:
            proba = (((1 - (data['length'] / some_length)) *
                      0.05) + (data['pheromone'] / somme_pheromones * 0.95))
            probs.append(proba)
            arrives.append(node2)

    if len(arrives) == 0:
        return -1

    probs = np.array(probs)
    probs /= probs.sum()
    res = choice(arrives, size=1, p=probs)[0]

    return res


def spread_pheromone(visited_nodes):
    graph_path_length = G.size(weight='length')
    distance = 0
    node_iterations = iter(visited_nodes)
    previous_node = next(node_iterations)

    for n in node_iterations:
        distance += G[previous_node][n]['length']
        previous_node = n

    pheromone_qty = graph_path_length / distance
    node_iterations = iter(visited_nodes)
    previous_node = next(node_iterations)

    for n in node_iterations:
        G[previous_node][n]['pheromone'] += round(pheromone_qty)
        previous_node = n


def evaporate_pheromone():
    for node1, node2 in G.edges:
        G[node1][node2]['pheromone'] = round(G[node1]
                                             [node2]['pheromone'] * 0.05)


def get_shortest_path():
    path = [FINISH_NODE]
    node = FINISH_NODE
    attempts = 0
    while node != START_NODE:
        maximum = 0
        attempts += 1

        if attempts > 1000:
            print('Missed')
            print(path)
            return None

        for node1, node2, data in G.edges(node, data=True):
            if data['pheromone'] > maximum and node2 not in path:
                maximum = data['pheromone']
                node = node2

        path.append(node)

    # Filter if node is or is not in found path
    nodes_not_in_path = [(u, v) for (u, v, d) in G.edges(data=True) if u not in path or v not in path]
    nodes_in_path = [(u, v) for (u, v, d) in G.edges(data=True) if u in path and v in path]

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=250)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=nodes_not_in_path,
                           width=2)
    nx.draw_networkx_edges(G, pos, edgelist=nodes_in_path,
                           width=3, edge_color=(200.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0))

    # labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    print(f'Shortest path: {path}')


def main():
    print(f"Start Node : {START_NODE} | End Node : {FINISH_NODE}")
    init()
    print("🟢 Started")
    launch()
    print("🔴 Ended")


if __name__ == '__main__':
    main()
