from collections import defaultdict


def check_connection(network, first, second):
    network = map(lambda x: x.split('-'), network)
    graph = create_graph(network)
    if second in dfs(first, graph):
        return True
    return False


def create_graph(network):
    graph = defaultdict(set)
    for edge in network:
        graph[edge[0]] |= set([edge[1]])
        graph[edge[1]] |= set([edge[0]])
    return graph


def dfs(first, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(first)
    for node in graph[first] - visited:
        dfs(node, graph, visited)
    return visited


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
