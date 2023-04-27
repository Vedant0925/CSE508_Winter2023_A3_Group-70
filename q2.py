import networkx as nx

#read the graph from the file
G = nx.read_edgelist('Wiki-Vote.txt', create_using=nx.DiGraph(), nodetype=int)

#calculate PageRank score for each node
pr = nx.pagerank(G)

#writing the PageRank score to a file
with open('pagerank_scores.txt', 'w') as f:
    for node, score in pr.items():
        f.write(f"Node: {node} Score: {score}\n")

#calculate authority and hub score for each node
hub, auth = nx.hits(G)

#write the Authority and Hub score to file
with open('auth_hub_scores.txt', 'w') as f:
    for node in G.nodes():
        f.write(f"Node: {node} Authority: {auth[node]} Hub: {hub[node]}\n")

#printing the number of nodes and edges
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

#reading scores from the output files
pagerank_scores = {}
with open('pagerank_scores.txt', 'r') as f:
    for line in f:
        node, score = line.split(" Score: ")
        node = int(node.replace("Node: ", ""))
        score = float(score.strip())
        pagerank_scores[node] = score

auth_hub_scores = {}
with open('auth_hub_scores.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(" ")
        node = int(parts[1])
        authority = float(parts[3])
        hub = float(parts[5])
        auth_hub_scores[node] = (authority, hub)

#sorting nodes by their scores
sorted_pr = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
sorted_auth = sorted(auth_hub_scores.items(), key=lambda x: x[1][0], reverse=True)
sorted_hub = sorted(auth_hub_scores.items(), key=lambda x: x[1][1], reverse=True)

#comparing top 10 nodes for each algorithm
n = 10
print(f"Top {n} nodes by PageRank:")
for i in range(n):
    node = sorted_pr[i][0]
    score = sorted_pr[i][1]
    print(f"Node {node} - Score: {score}")
    print("Outgoing links:", len(list(G.successors(node))))
    print("Incoming links:", len(list(G.predecessors(node))))
    print()

print(f"\nTop {n} nodes by Authority:")
for i in range(n):
    node = sorted_auth[i][0]
    authority = sorted_auth[i][1][0]
    print(f"Node {node} - Authority: {authority}")
    print("Outgoing links:", len(list(G.successors(node))))
    print("Incoming links:", len(list(G.predecessors(node))))
    print()

print(f"\nTop {n} nodes by Hub:")
for i in range(n):
    node = sorted_hub[i][0]
    hub = sorted_hub[i][1][1]
    print(f"Node {node} - Hub: {hub}")
    print("Outgoing links:", len(list(G.successors(node))))
    print("Incoming links:", len(list(G.predecessors(node))))
    print()
