import networkx as nx
import matplotlib.pyplot as plt
import random 

def star_graph(n0: int) -> nx.Graph:
    """
    Create a star graph with n0 nodes.
    All nodes will be connected to the center node with index 0

    :param n0: NUmber of nodes in the initial star graph
    :return: star graph that reprensents a netwerk graph
    """
    graph = nx.Graph()\
    
    for i in range(1, n0):
        graph.add_edge(0, i)

    return graph

def new_node_barabasi_albert(graph: nx.Graph, M: int) -> None:
    """
    Add a new node to the graph that connects to M nodes.
    new node is connected with probability proportional to node degree

    :param graph: the existing graph
    :param M: number of edges to add to a new node
    """
    new_node = len(graph.nodes)
    e_nodes = list(graph.nodes)

    #the degree of the nodes
    degree_nodes = [graph.degree(node) for node in e_nodes]
    t_degree = sum(degree_nodes)

    # chosing M unique nodes to connect to the new node

    chosen_nodes = set()

    while len(chosen_nodes) < M:
        target = random.choices(e_nodes, weight = degree_nodes, k=1)[0]
        if target not in chosen_nodes and target != new_node:
            chosen_nodes.add(target)

    