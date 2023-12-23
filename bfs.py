from collections import deque


def bfs(graph, start_node, target_node):
    visited = set()
    queue = deque([(start_node, [start_node])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == target_node:
            return path

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node - 1]['neighbors']
            for neighbor in neighbors:
                neighbor_id = neighbor['id']
                if neighbor_id not in visited:
                    queue.append((neighbor_id, path + [neighbor_id]))

    return None
