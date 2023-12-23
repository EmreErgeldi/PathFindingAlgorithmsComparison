from bfs import bfs
from dfs import dfs
from graph import graph


def main():
    start_node = int(input("Baslangic sehrini giriniz: "))
    target_node = int(input("Hedef sehri giriniz: "))

    # BFS
    result_bfs = bfs(graph, start_node, target_node)

    if result_bfs:
        print("BFS Yol:", result_bfs)
    else:
        print("BFS Yolu bulunamadi.")

    # DFS
    result_dfs = dfs(graph, start_node, target_node)

    if result_dfs:
        print("DFS Yol:", result_dfs)
    else:
        print("DFS Yol bulunamadi.")


if __name__ == "__main__":
    main()
