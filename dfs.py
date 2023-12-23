def dfs(graph, start_node, target_node):
    visited = set()
    stack = [(start_node, [start_node])]

    while stack:
        current_node, path = stack.pop()

        if current_node == target_node:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node - 1]['neighbors']  # Adjust index for 0-based indexing
            for neighbor in neighbors:
                neighbor_id = neighbor['id']
                if neighbor_id not in visited:
                    stack.append((neighbor_id, path + [neighbor_id]))

    return None
