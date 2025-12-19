import tsplib95

problem = tsplib95.load("instances/tsp_5.tsp")

print(problem.name)
print(problem.dimension)
print(problem.node_coords)
