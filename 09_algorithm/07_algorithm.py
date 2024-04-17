#7▹ Zaimplementuj w Pythonie algorytm Dijkstry.

# Przyznam się że algorytmy nie są moją mocną stroną i przy niektórych pracahc inspirowałem się rozwiązaniami z interneru :(

def dij(nodes, edg, src=0):
    path_len = {v: float("inf") for v in nodes}
    path_len[src] = 0
    adj_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edg.items():
        adj_nodes[u][v] = w_uv
        adj_nodes[v][u] = w_uv
    temp_nodes = [v for v in nodes]
    while len(temp_nodes) > 0:
        uper_bounds = {v : path_len[v] for v in temp_nodes}
        u = min(uper_bounds, key=uper_bounds.get)
        temp_nodes.remove(u)
        for v , w_uv in adj_nodes[u].items():
            path_len[v] = min(path_len[v], path_len[u] + w_uv)

    return path_len


vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges = [[0, 3, 4, 0],
          [0, 0, 0.5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]
print(dij(vertices,edges))