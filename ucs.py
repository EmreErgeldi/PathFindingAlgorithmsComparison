import heapq
import graph as map

graph = map.graph

def get_city_id_by_name(graph, city_name):
    for city in graph:
        if city['name'].lower() == city_name.lower():
            return city['id']
    return None

def uniform_cost_search(graph, start_city_name, goal_city_name):
    start_id = get_city_id_by_name(graph, start_city_name)
    goal_id = get_city_id_by_name(graph, goal_city_name)

    if start_id is None or goal_id is None:
        return float('inf'), [], 0

    visited = set()
    heap = [(0, start_id, [start_id])]
    node_count = 0  # Sayaç başlatılır
    while heap:
        (cost, current_id, path) = heapq.heappop(heap)
        if current_id in visited:
            continue
        visited.add(current_id)
        print(f"Şu an {graph[current_id - 1]['name']} şehrindeyiz.")
        node_count += 1  # Her adımda bir node'a uğranıldığında sayaç arttırılır
        if current_id == goal_id:
            return cost, path, node_count
        neighbors = graph[current_id - 1]['neighbors']
        for neighbor in neighbors:
            neighbor_id = neighbor['id']
            if neighbor_id not in visited:
                new_cost = cost + neighbor['distance']
                new_path = path + [neighbor_id]
                heapq.heappush(heap, (new_cost, neighbor_id, new_path))
    return float('inf'), [], 0  # If the goal is not reachable

while True:
    print("######################## Şehirler Arasi Mesafe Hesaplama - Uniform Cost Search (Çikis yapmak için 'q' giriniz) #########################")
    start_city_name = input("Başlangiç Şehri: ")
    goal_city_name = input("Hedef Şehir: ")
    
    if start_city_name == "q" or goal_city_name == "q":
        break

    distance, path, node_count = uniform_cost_search(graph, start_city_name, goal_city_name)

    if distance == float('inf'):
        print(f"Geçersiz Şehir, Tekrar Deneyiniz...")
    else:
        print(f"Hesaplanan mesafe: {distance} km.")
        print(f"Ziyaret Edilen Şehirler: {', '.join([graph[node - 1]['name'] for node in path])}")
        print(f"Toplam {node_count} adet şehir(düğüm) ziyaret edildi.")
