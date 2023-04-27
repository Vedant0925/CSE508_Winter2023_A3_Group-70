def read_edges(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line.strip().split() for line in lines if not line.startswith("#")]

    edges = [(int(line[0]), int(line[1])) for line in lines]
    return edges

def create_adjacency_list(edges):
    adjacency_list = {}
    for u, v in edges:
        if u not in adjacency_list:
            adjacency_list[u] = []
        adjacency_list[u].append(v)
    return adjacency_list

file_path = "/Users/vedant/Downloads/wiki-Vote.txt"
edges = read_edges(file_path)


adj_matrix = create_adjacency_list(edges)

# Finding number of nodes
def number_of_nodes(adjacency_list):
    nodes = set(adjacency_list.keys())
    for neighbors in adjacency_list.values():
        nodes.update(neighbors)
    return len(nodes)

# for number of edges
def number_of_edges(edges):
    return len(edges)

# calculating in-degree and out-degree
def in_out_degrees(edges):
    in_degrees = {}
    out_degrees = {}
    for u, v in edges:
        out_degrees[u] = out_degrees.get(u, 0) + 1
        in_degrees[v] = in_degrees.get(v, 0) + 1
    return in_degrees, out_degrees

# Calculating average in-degree and out-degree
def avg_in_out_degrees(in_degrees, out_degrees, num_nodes):
    total_in_degree = sum(in_degrees.values())
    total_out_degree = sum(out_degrees.values())
    avg_in_degree = total_in_degree / num_nodes
    avg_out_degree = total_out_degree / num_nodes
    return avg_in_degree, avg_out_degree

# finding nodes with maximum in-degree and out-degree
def max_in_out_degree(in_degrees, out_degrees):
    max_in_degree_node = max(in_degrees, key=in_degrees.get)
    max_out_degree_node = max(out_degrees, key=out_degrees.get)
    return max_in_degree_node, max_out_degree_node

# Finding the network density
def network_density(num_nodes, num_edges):
    density = num_edges / (num_nodes * (num_nodes - 1))
    return density

# Load the dataset
file_path = "/Users/vedant/Downloads/wiki-Vote.txt"
edges = read_edges(file_path)

# Create adjacency list representation
adjacency_list = create_adjacency_list(edges)


num_nodes = number_of_nodes(adjacency_list)
num_edges = number_of_edges(edges)
in_degrees, out_degrees = in_out_degrees(edges)
avg_in_degree, avg_out_degree = avg_in_out_degrees(in_degrees, out_degrees, num_nodes)
max_in_degree_node, max_out_degree_node = max_in_out_degree(in_degrees, out_degrees)
density = network_density(num_nodes, num_edges)


print(f"1. Number of Nodes: {num_nodes}")
print(f"2. Number of Edges: {num_edges}")
print(f"3. Avg In-degree: {avg_in_degree}")
print(f"4. Avg. Out-Degree: {avg_out_degree}")
print(f"5. Node with Max In-degree: {max_in_degree_node}")
print(f"6. Node with Max out-degree: {max_out_degree_node}")
print(f"7. The density of the network: {density}")

import matplotlib.pyplot as plt

# Load the dataset
with open(file_path, 'r') as file:
    lines = file.readlines()

# Here we have Initialized our dictionaries for in-degree and out-degree
in_degree = {}
out_degree = {}

# Iterate the for loop through each line of the given txt file of the dataset
for line in lines:
    if line.startswith("#"):
        continue
        # Skip comment lines
    tokens = [[] * 2]
    tokens[0] = line.split()
    source, target = tokens[0][0], tokens[0][
        1]  ## we will consider elements of source and target of connections between the nodes

    # Increment out-degree of source node in the dictionary if yes increment else add it
    if source in out_degree:
        out_degree[source] += 1
    else:
        out_degree[source] = 1

    # Increment in-degree of target node in the dictionary if yes increment else add it
    if target in in_degree:
        in_degree[target] += 1
    else:
        in_degree[target] = 1

# Compute the maximum degree in the network which is the maximum value among the degrees of all the nodes in the network.
max_degree = max(max(in_degree.values()), max(out_degree.values()))

# Compute the frequency of each degree
out_degree_freq = [[] * 2]
in_degree_freq = [[] * 2]
out_degree_freq[0] = [0] * (max_degree + 1)
in_degree_freq[0] = [0] * (max_degree + 1)
# It counts the frequency of each out-degree and in-degree value in the network.


for degree in out_degree.values():
    out_degree_freq[0][degree] += 1

for degree in in_degree.values():
    in_degree_freq[0][degree] += 1

# Add counts for zero degrees
out_degree_freq[0][0] = len(set(out_degree.keys()) - set(in_degree.keys()))
in_degree_freq[0][0] = len(set(in_degree.keys()) - set(out_degree.keys()))

# Plot out-degree distribution as a bar graph
plt.figure()
plt.bar(range(max_degree + 1), in_degree_freq[0], width=1, edgecolor='blue')

plt.title("In-degree Distribution")
plt.xlabel("In-degree")
plt.ylabel("Frequency")
plt.show()
