def check_connection(network, first, second):
    network = map(lambda x: x.split('-'), network)
    queue = set([first])
    return traverse(queue, network, second)


def traverse(queue, network, second):
    if len(queue) == 0:
        return False
    new_queue = set([])
    new_network = []
    for target in queue:
        for edge in network:
            if target in edge:
                node = get_node(edge, target)
                if node == second:
                    return True
                new_queue.add(get_node(edge, target))
            else:
                if (not edge in new_network) and (not set(edge) in queue):
                    new_network.append(edge)
    return traverse(new_queue, new_network, second)


def get_node(edge, char):
    if edge[0] == char:
        return edge[1]
    else:
        return edge[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "scout2", "scout3") == True, "Scout Brotherhood"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "super", "scout2") == True, "Super Scout"
    # assert check_connection(
    #     ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
    #      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    #     "dr101", "sscout") == False, "I don't know any scouts."
    print check_connection(("a-b","b-c","c-d","d-e","e-a"),"a","e")
    # check_connection(("sscout-batman", "plane1-scout3", "stevan-batman",
    #                   "super-sscout", "scout2-batman", "scout2-sscout",
    #                   "doc-mega", "night-batman", "scout3-doc",), "scout2",
    #                  "plane1")
