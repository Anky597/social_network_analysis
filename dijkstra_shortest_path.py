def dijkstra_shortest_path(G, start_node, end_node):
    distances = {node: float('inf') for node in G}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    previous_nodes = {node: None for node in G}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in G[current_node]:
            weight = G[current_node][neighbor]['weight']
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
#code for Dijkstra shortest path;
