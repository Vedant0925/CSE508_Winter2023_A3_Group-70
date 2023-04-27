import networkx as nx
import matplotlib.pyplot as plt


# Read the graph from the file
G = nx.read_edgelist('Wiki-Vote.txt', create_using=nx.DiGraph(), nodetype=int)

# Calculate PageRank score for each node
pr = nx.pagerank(G)

# Write the PageRank score to a file
with open('pagerank_scores.txt', 'w') as f:
    for node, score in pr.items():
        f.write(f"Node: {node} Score: {score}\n")

# Calculate Authority and Hub score for each node
auth, hub = nx.hits(G)

# Write the Authority and Hub score to a file
with open('auth_hub_scores.txt', 'w') as f:
    for node in G.nodes():
        f.write(f"Node: {node} Authority: {auth[node]} Hub: {hub[node]}\n")

# Print the number of nodes and edges
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())


