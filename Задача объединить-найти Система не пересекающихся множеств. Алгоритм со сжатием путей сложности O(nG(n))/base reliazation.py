def init(count_sets: int):
    global parents
    for set_id in range(count_sets):
        parents.append(set_id)


def find(node: int) -> int:
    global parents
    if node == parents[node]:
        return node
    return find(parents[node])


def union(set_to_connect: int, set_connector: int):
    global parents
    set_connector_parent = find(set_connector)
    set_to_connect_parent = find(set_to_connect)
    if set_connector_parent != set_to_connect_parent:
        parents[set_to_connect_parent] = set_connector_parent


parents = []
