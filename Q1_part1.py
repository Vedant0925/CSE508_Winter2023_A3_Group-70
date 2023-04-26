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

def number_of_nodes(adjacency_list):
    nodes = set(adjacency_list.keys())
    for neighbors in adjacency_list.values():
        nodes.update(neighbors)
    return len(nodes)

def number_of_edges(edges):
    return len(edges)


def in_out_degrees(edges):
    in_degrees = {}
    out_degrees = {}
    for u, v in edges:
        out_degrees[u] = out_degrees.get(u, 0) + 1
        in_degrees[v] = in_degrees.get(v, 0) + 1
    return in_degrees, out_degrees


def avg_in_out_degrees(in_degrees, out_degrees, num_nodes):
    total_in_degree = sum(in_degrees.values())
    total_out_degree = sum(out_degrees.values())
    avg_in_degree = total_in_degree / num_nodes
    avg_out_degree = total_out_degree / num_nodes
    return avg_in_degree, avg_out_degree


def max_in_out_degree(in_degrees, out_degrees):
    max_in_degree_node = max(in_degrees, key=in_degrees.get)
    max_out_degree_node = max(out_degrees, key=out_degrees.get)
    return max_in_degree_node, max_out_degree_node


def network_density(num_nodes, num_edges):
    density = num_edges / (num_nodes * (num_nodes - 1))
    return density


file_path = "/Users/vedant/Downloads/wiki-Vote.txt"
edges = read_edges(file_path)


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
