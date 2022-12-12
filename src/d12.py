#%%
import string
import networkx as nx

heights = dict(
    zip(string.ascii_lowercase, [i for i in range(1, len(string.ascii_letters) + 1)])
)
heights["S"], heights["E"] = 1, 26
with open("../data/d12.txt", "r") as f:
    grid = [x.rstrip() for x in f.read().split("\n")]

# map each point in grid to it's coordinate
all_coords, start, end = {}, (), ()

# Pull out coordinates and height values, as well as start and end coordinates
for i in range(len(grid)):
    for j in range(len(grid[0])):
        all_coords[(i, j)] = heights[grid[i][j]]
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "E":
            end = (i, j)

graph = nx.DiGraph()

for coords, val in all_coords.items():
    i, j = coords[0], coords[1]
    # Search all directions
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i, new_j = i + di, j + dj
        # Qualify the comparison coordinate
        if new_i in [-1, len(grid)] or new_j in [-1, len(grid[0])]:
            continue
        # Add edge to graph
        if all_coords[(i, j)] >= all_coords[(new_i, new_j)] - 1:
            graph.add_edge(u_of_edge=(i, j), v_of_edge=(new_i, new_j))

shortest_path = len(nx.shortest_path(graph, start, end)) - 1
print("Part 1:", shortest_path)

# Use same graph as above to map lengths of paths where starting point height == 1
a_paths = [
    length
    # returns shortest path for each node in the graph to the end you pass
    for c, length in nx.single_target_shortest_path_length(graph, end)
    # Qualify that starting point was the lowest it can be (==1)
    if all_coords[c] == 1
]

print(f"Part 2: {min(a_paths)}")
