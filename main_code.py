import heapq
import matplotlib.pyplot as plt

def load_sample_graph():
    graph = {
        "Alice": {"Bob": 1, "Charlie": 1, "David": 1},
        "Bob": {"Alice": 1, "Charlie": 1, "Eve": 1, "Grace": 1},
        "Charlie": {"Alice": 1, "Bob": 1, "David": 1, "Frank": 1, "Hannah": 1},
        "David": {"Alice": 1, "Charlie": 1, "Ian": 1},
        "Eve": {"Bob": 1, "Frank": 1, "Jack": 1},
        "Frank": {"Charlie": 1, "Eve": 1, "Kathy": 1},
        "Grace": {"Bob": 1, "Liam": 1},
        "Hannah": {"Charlie": 1, "Mia": 1},
        "Ian": {"David": 1, "Nina": 1},
        "Jack": {"Eve": 1, "Oscar": 1},
        "Kathy": {"Frank": 1, "Paul": 1},
        "Liam": {"Grace": 1, "Quinn": 1},
        "Mia": {"Hannah": 1, "Rita": 1},
        "Nina": {"Ian": 1, "Steve": 1},
        "Oscar": {"Jack": 1, "Tom": 1},
        "Paul": {"Kathy": 1, "Uma": 1},
        "Quinn": {"Liam": 1, "Vera": 1},
        "Rita": {"Mia": 1, "Will": 1},
        "Steve": {"Nina": 1, "Xena": 1},
        "Tom": {"Oscar": 1, "Yara": 1},
        "Uma": {"Paul": 1, "Zara": 1},
        "Vera": {"Quinn": 1},
        "Will": {"Rita": 1},
        "Xena": {"Steve": 1},
        "Yara": {"Tom": 1},
        "Zara": {"Uma": 1}
    }
    return graph

def bfs_traversal(graph, start_node):
    visited = set()
    queue = [start_node]
    edges = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    edges.append((node, neighbor))

    return edges

def dfs_traversal(graph, start_node):
    visited = set()
    stack = [start_node]
    edges = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(neighbor)
                    edges.append((node, neighbor))

    return edges

def dijkstra_shortest_path(graph, start_node, end_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path, node = [], end_node
    while previous_nodes[node] is not None:
        path.insert(0, node)
        node = previous_nodes[node]
    if path:
        path.insert(0, start_node)

    return path

def calculate_centrality(graph):
    degree_centrality = {node: len(neighbors) for node, neighbors in graph.items()}
    betweenness_centrality = {node: 0 for node in graph}  # Simplified version
    closeness_centrality = {node: 0 for node in graph}  # Simplified version
    return degree_centrality, betweenness_centrality, closeness_centrality

def visualize_graph(graph):
    import networkx as nx

    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray')
    plt.show()

# Test the code

# Load the sample graph
graph = load_sample_graph()

# Perform BFS Traversal
bfs_result = bfs_traversal(graph, "Alice")
print("BFS Traversal: ", bfs_result)

# Perform DFS Traversal
dfs_result = dfs_traversal(graph, "Alice")
print("DFS Traversal: ", dfs_result)

# Perform Dijkstra's Shortest Path
dijkstra_result = dijkstra_shortest_path(graph, "Alice", "Zara")
print("Shortest Path from Alice to Zara: ", dijkstra_result)

# Calculate Centrality Measures
degree_centrality, betweenness_centrality, closeness_centrality = calculate_centrality(graph)
print("Degree Centrality: ", degree_centrality)
print("Betweenness Centrality: ", betweenness_centrality)
print("Closeness Centrality: ", closeness_centrality)

# Visualize the Graph
visualize_graph(graph)
