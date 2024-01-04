import time

from bfs_dfs import bfs, dfs
from graph import graph

from ucs import uniform_cost_search

def main():
    start_node = input("Başlangıç şehrini giriniz: ")
    target_node = input("Hedef şehri giriniz: ")

    # BFS
    bfs_start_time = time.perf_counter_ns()
    result_bfs = bfs(graph, start_node, target_node)
    bfs_end_time = time.perf_counter_ns()

    if result_bfs:
        print(f"BFS Yol: {result_bfs}")
        print(f"BFS Zaman: {bfs_end_time - bfs_start_time} ns")
    else:
        print("BFS Yolu bulunamadı.")

    # DFS
    dfs_start_time = time.perf_counter_ns()
    result_dfs = dfs(graph, start_node, target_node)
    dfs_end_time = time.perf_counter_ns()

    if result_dfs:
        print(f"DFS Yol: {result_dfs}")
        print(f"DFS Zaman: {dfs_end_time - dfs_start_time} ns")
    else:
        print("DFS Yol bulunamadı.")

    # UCS
    print("\n\n########################## Uniform Cost Search ##########################")
    ucs_start_time = time.perf_counter_ns()
    distance, path, node_count = uniform_cost_search(graph, start_node, target_node)
    ucs_end_time = time.perf_counter_ns()

    if distance == float('inf'):
        print(f"Geçersiz Şehir, Tekrar Deneyiniz...")
    else:
        print(f"Hesaplanan mesafe: {distance} km.")
        print(f"Bulunan Yol: {' -> '.join([graph[node - 1]['name'] for node in path])}")
        print(f"Toplam {node_count} adet şehir(düğüm) ziyaret edildi.")
        print(f"Toplam Süre: {ucs_end_time - ucs_start_time} ns.")


if __name__ == "__main__":
    main()
