#%%
import string

heights = dict(
    zip(string.ascii_lowercase, [i for i in range(1, len(string.ascii_letters) + 1)])
)
with open("../data/d12.txt", "r") as f:
    grid = [x.rstrip() for x in f.read().split("\n")]

h = len(grid)
w = len(grid[0])

start = ()

for y in range(0, h):
    for x in range(0, w):
        if grid[y][x] == "S":
            start = (x, y)

# moves =
