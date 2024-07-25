def dfs_traversal(G, start_node):
    visited = set()
    stack = [start_node]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            stack.extend(n for n in G[node] if n not in visited)

    return traversal

#code for the DFS traversal;
