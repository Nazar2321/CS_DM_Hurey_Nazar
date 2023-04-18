def read_graph(filename):
    with open(filename, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]

graph1 = read_graph('graph1.txt')
graph2 = read_graph('graph2.txt')

if len(graph1) != len(graph2) or any(len(row1) != len(row2) for row1, row2 in zip(graph1, graph2)):
    print("Not isomorphic")
else:
    is_isomorphic = all((elem1 == 0) == (elem2 == 0) for row1, row2 in zip(graph1, graph2) for elem1, elem2 in zip(row1, row2))
    print("Isomorphic" if is_isomorphic else "Not isomorphic")