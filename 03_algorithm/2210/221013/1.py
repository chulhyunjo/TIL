graph = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
new_graph = list(map(list,zip(*graph)))
print(new_graph)
print(graph)