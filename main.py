import networkx as nx
import random


def make_de_bruijn_graph(k, patterns):
    global G
    G = nx.Graph()
    for pattern in patterns:
        for i in range(len(pattern) - k + 1):
            kmer = pattern[i:i + k]
            G.add_edge(kmer[:-1], kmer[1:])
    return G


def evaluate_fragility(graph, num_attacks, attack_size):
    """
  Evaluates the fragility of the given de Bruijn graph by simulating the removal of
  a certain number of randomly selected nodes and measuring the size of the largest
  connected component after each removal.
  """
    largest_cc_sizes = []
    num_nodes = len(graph)

    # Debugging line
    # print("Number of nodes:", num_nodes)
    # print("Attack size:", attack_size)
    for i in range(num_attacks):
        if attack_size > num_nodes or attack_size < 0:
            raise ValueError("Invalid attack size")
        # Select a random set of nodes to remove
        attack_nodes = random.sample(list(graph.nodes), attack_size)
        # Remove the selected nodes from the graph
        graph.remove_nodes_from(attack_nodes)
        # Measure the size of the largest connected component
        largest_cc_size = max([len(cc) for cc in nx.connected_components(graph)])
        largest_cc_sizes.append(largest_cc_size)
        # Add the removed nodes back to the graph
        graph.add_nodes_from(attack_nodes)
    return largest_cc_sizes


def evaluate_resilience(graph, num_attacks, attack_size):
    """
  Evaluates the resilience of the given de Bruijn graph by simulating the removal of
  a certain number of randomly selected nodes and measuring the size of the graph
  after each removal.
  """
    graph_sizes = []
    num_nodes = len(graph)
    # Debugging line
    # print("Number of nodes:", num_nodes)
    # print("Attack size:", attack_size)
    for i in range(num_attacks):
        if attack_size > num_nodes or attack_size < 0:
            raise ValueError("Invalid attack size")
        # Select a random set of nodes to remove
        attack_nodes = random.sample(list(graph.nodes), attack_size)
        # Remove the selected nodes from the graph
        graph.remove_nodes_from(attack_nodes)
        # Measure the size of the graph
        graph_size = len(graph)
        graph_sizes.append(graph_size)
        # Add the removed nodes back to the graph
        graph.add_nodes_from(attack_nodes)
    return graph_sizes


# Take the graph
numbers = int(input("How many gnomes do you need? "))
patterns = []
for iterations in range(0, numbers):
    patterns.append(input(f"Write down number -> {iterations + 1} gnome. For Example AACC or AGGGB: "))
print("--------------------------------------------------------------")
print(f"Your patterns according to your inputs are {patterns} ")

# take the k-value (character number)
k_value = int(input("Please write the K-value: "))
G = make_de_bruijn_graph(k_value, patterns)
print(G)

# Print the edges of the graph
print("--------------------------------------------------------------")
print(f" The DeBruijn Graph Edges are= \n{G.edges()}")

# number of attacks & size of the attacks considered 1. We can change them
number_of_attacks = int(input("Please Enter number of Attacks: "))
size_of_attack = int(input("Please Enter Size of the Attacks: "))
fragility_scores = evaluate_fragility(G, num_attacks=number_of_attacks, attack_size=size_of_attack)
resilience_scores = evaluate_resilience(G, num_attacks=number_of_attacks, attack_size=size_of_attack)
print("--------------------------------------------------------------")
print(f"Fragility Score is= {fragility_scores}")
print(f"Resilience Score is= {resilience_scores}")