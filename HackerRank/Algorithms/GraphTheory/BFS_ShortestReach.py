# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
EDGE_LEN = 6


def print_distances(distances):
    # print distances
    for d in distances[1:]:
        if d != 0:
            print d,
    print ""


def shortest_paths(graph, start):
    distances = [-1]*(len(graph))
    distances[start] = 0
    on_deck = deque()
    on_deck.append(start)
    while len(on_deck):
        curr = on_deck.popleft()
        curr_dist = distances[curr] + EDGE_LEN
        for node in graph[curr]:
            if distances[node] < 0:
                distances[node] = curr_dist
                on_deck.append(node)

    print_distances(distances, start)

num_queries = input()
for _ in xrange(num_queries):
    num_nodes, num_edges = map(int, raw_input().split())
    graph = [None]*(num_nodes + 1)
    for _ in xrange(num_edges):
        one, two = map(int, raw_input().split())
        if graph[one] is None:
            graph[one] = set()
        if graph[two] is None:
            graph[two] = set()
        graph[one].add(two)
        graph[two].add(one)
    s = input()
    shortest_paths(graph, s)
