def init(count_sets: int):
    global parents
    for set_id in range(count_sets):
        parents.append(set_id)
        rank.append(1)


def find(node: int) -> int:
    global parents
    if node != parents[node]:
        parents[node] = find(parents[node])
    return parents[node]


def union(set_to_connect: int, set_connector: int):
    global parents
    set_connector_parent = find(set_connector)
    set_to_connect_parent = find(set_to_connect)
    if set_connector_parent != set_to_connect_parent:
        if rank[set_connector_parent] < rank[set_to_connect]:
            set_connector_parent, set_to_connect_parent = set_to_connect_parent, set_connector_parent
        parents[set_to_connect_parent] = set_connector_parent
        if rank[set_connector_parent] == rank[set_to_connect_parent]:
            rank[set_connector_parent] += 1


parents = []
rank = []