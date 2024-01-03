import heapq
import time
import matplotlib.pyplot as plt
from turkiye import graph

def get_city_id_by_name(graph, city_name):
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def dijkstra(graph, start, goal):
    start_time = time.perf_counter_ns()

    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        current_cost, current_city, path = heapq.heappop(priority_queue)

        if current_city == goal:
            end_time = time.perf_counter_ns()
            print("Path found!")
            for city in path:
                print(graph[city - 1]["name"])
            print("Total Time:", end_time - start_time, "nano seconds")

            # Entegrasyon: En kısa yolu çiz
            plot_path(graph, path)
            return

        if current_city in visited:
            continue

        visited.add(current_city)

        for neighbor in graph[current_city - 1]["neighbors"]:
            neighbor_id = neighbor["id"]
            new_cost = current_cost + neighbor["distance"]

            heapq.heappush(
                priority_queue, (new_cost, neighbor_id, path + [neighbor_id])
            )

    end_time = time.perf_counter_ns()
    print("No path found!")
    print("Total Time:", end_time - start_time, "nano seconds")


def plot_path(graph, path):
    # Visualise
    x, y = [], []
    for i in path:
        x.append(graph[i - 1]["lon"])
        y.append(graph[i - 1]["lat"])
        plt.text(graph[i - 1]["lon"], graph[i - 1]["lat"], graph[i - 1]["name"])

    x.append(x[0])
    y.append(y[0])
    plt.title("Dijkstra Algorithm")
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()
    plt.draw()


# Example usage:
start_city_name = input("Enter the current city: ")
goal_city_name = input("Enter the goal city: ")

# Find city IDs based on city names
start_city = get_city_id_by_name(graph, start_city_name)
goal_city = get_city_id_by_name(graph, goal_city_name)

# Run Dijkstra's algorithm
dijkstra(graph, start_city, goal_city)
