import heapq

def prum(graph_file):
    with open(graph_file) as f:
        lines = f.readlines()
        n = int(lines[0])
        graph = [list(map(int, line.strip().split())) for line in lines[1:]]

    visited = [0]
    mst = []
    possible_edges = [(graph[0][j], 0, j) for j in range(1, n)]

    while len(mst) < n-1:
        w, u, v = heapq.heappop(possible_edges)
        if v not in visited:
            visited.append(v)
            mst.append((u, v, w))
            for j in range(n):
                if graph[v][j] != 0 and j not in visited:
                    heapq.heappush(possible_edges, (graph[v][j], v, j))

    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

prum("graph.txt")