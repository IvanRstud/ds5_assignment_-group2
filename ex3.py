import networkx as nx
import matplotlib.pyplot as plt
import random 
import matplotlib.cm as cm
import matplotlib.colors as mcolors

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
        target = random.choices(e_nodes, weights = degree_nodes, k=1)[0]
        if target not in chosen_nodes and target != new_node:
            chosen_nodes.add(target)

    for target in chosen_nodes:
        graph.add_edge(new_node, target)

def generate_barabasi_albert(n0: int, N: int, M: int) -> nx.Graph:
    """
    Generate a Barabasi albert network

    :param n0: Initial number of nodes
    :param N: total number of nodes
    :param M: Number of edges each new node should have
    :return: A graph object representing a Barabasi albert network
    """
    graph = star_graph(n0)

    while len(graph.nodes) < N:
        new_node_barabasi_albert(graph, M)

    return graph

def calculate(graph: nx.Graph) -> dict:
    """
    calculate the PageRank of each node

    :param graph: the input graph
    :return: the PageRank values of the corresponding nodes
    """
    return nx.pagerank(graph)

def visualisation(graph: nx.Graph, pagerank: dict) -> None:
    """
    Visualising the graph and the PageRank

    :param graph: the graph to visualize
    :param pagerank: The PageRank values
    """
    plt.figure(figsize=(10, 8))
    
    # Node size based on PageRank (larger size = higher PageRank)
    node_size = [pagerank[node] * 5000 for node in graph.nodes]
    
    # Use a fixed node color, e.g., light blue
    node_color = "lightblue"
    
    # Create a layout for the graph
    pos = nx.spring_layout(graph)  # Layout for visualization
    
    # Draw the network with node sizes based on PageRank values
    nx.draw_networkx_nodes(graph, pos, node_size=node_size, node_color=node_color, edgecolors="black")
    nx.draw_networkx_edges(graph, pos)
    
    # Draw node labels with the PageRank value rounded to 3 decimal places
    labels = {node: f"{pagerank[node]:.3f}" for node in graph.nodes}
    nx.draw_networkx_labels(graph, pos, labels, font_size=8)
    
    plt.title("Barabasi-Albert Network with Node Size Proportional to PageRank and Labeled Values")
    plt.show()


def plot_pagerank(pagerank: dict) -> None:
        """
        Visualizing the PageRank distribution

        :param pagerank: the PageRank values for each node
        """

        plt.figure(figsize=(8, 6))

        values = list(pagerank.values())
        plt.hist(values, bins=20, color="blue", edgecolor='black')

        plt.title("PageRank distribution")
        plt.xlabel("PageRank")
        plt.ylabel("Frequency")

        plt.show()

if __name__ == "__main__":

    n0 = 5    
    N = 400   
    M = 4     


    graph = generate_barabasi_albert(n0, N, M)
    
    # Calculate PageRank
    pagerank = calculate(graph)
    
    # Visualize the network and the PageRank distribution
    visualisation(graph, pagerank)
    plot_pagerank(pagerank)


