import time

from bfs_dfs import bfs, dfs
from graph import graph


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


if __name__ == "__main__":
    main()
