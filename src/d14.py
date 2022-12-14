#%%
def parse_data():
    with open("../data/d14.txt", "r") as f:
        paths = f.read().split("\n")

    # Extract rock coordinates
    rocks = []
    for path in paths:
        markers = path.split(" -> ")
        for i in range(len(markers) - 1):
            sx, sy = map(int, markers[i].split(","))
            ex, ey = map(int, markers[i + 1].split(","))
            if sx == ex:
                y_vals = sorted([sy, ey])
                range_y = list(range(y_vals[0], y_vals[1] + 1))
                coords = [(sx, y) for y in range_y]
                rocks.extend(coords)
            elif sy == ey:
                x_vals = sorted([sx, ex])
                range_x = list(range(x_vals[0], x_vals[1] + 1))
                coords = [(x, sy) for x in range_x]
                rocks.extend(coords)
    return rocks


def create_grid():
    rocks = parse_data()
    # Create Grid
    max_x = max(x for x, y in rocks)
    max_y = max(y for x, y in rocks)

    grid = [["."] * (max_x + 200) for i in range(max_y + 2)]
    grid.append(["#"] * (max_x + 200))
    grid[0][500] = "*"

    # Add rocks to grid
    for rock in rocks:
        grid[rock[1]][rock[0]] = "#"
    return max_x, max_y, grid


# max_x, max_y, grid = create_grid()

sand = "o"
open_air = "."


def drop_grains(part_2=False):
    grain_resting = False
    location = (500, 0)
    while grain_resting == False:
        w, h = location
        if not part_2 and h == max_y:
            break
        # Check under for open space
        elif grid[h + 1][w] == open_air:
            location = (w, h + 1)
        # Check under left and under right
        elif grid[h + 1][w - 1] != open_air and grid[h + 1][w + 1] != open_air:
            grid[h][w] = sand
            grain_resting = True
        # Check only left
        elif grid[h + 1][w - 1] == open_air:
            location = (w - 1, h + 1)
        # Check only right
        elif grid[h + 1][w + 1] == open_air:
            location = (w + 1, h + 1)
    return grain_resting


max_x, max_y, grid = create_grid()
p1_grain_count = 0
while True:
    if drop_grains():
        p1_grain_count += 1
    else:
        break


max_x, max_y, grid = create_grid()
p2_grain_count = 0
while grid[0][500] != "o":
    grain_resting = drop_grains(part_2=True)
    p2_grain_count += 1

print(f"Part 1: {p1_grain_count}\nPart 2: {p2_grain_count}")
