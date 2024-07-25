def bfs_traversal(G, start_node):
    visited = set()
    queue = [start_node]
    traversal = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(n for n in G[node] if n not in visited)

    return traversal

#code for BFS teversal.
