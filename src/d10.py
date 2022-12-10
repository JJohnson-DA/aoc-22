#%%
with open("../data/d10.txt", "r") as f:
    lines = [x.rstrip().split() for x in f.readlines()]

stop_points = [20, 60, 100, 140, 180, 220]

p1_total, cycle, X = 0, 0, 1
grid = [[" "] * 40 for i in range(6)]

for line in lines:
    current_point = cycle if cycle < 40 else (cycle - ((cycle // 40) * 40))
    if current_point in [X - 1, X, X + 1]:
        grid[int(cycle // 40)][current_point] = "#"
    cycle += 1
    if cycle in stop_points:
        p1_total += X * cycle
    if line[0] == "addx":
        current_point = cycle if cycle < 40 else (cycle - ((cycle // 40) * 40))
        if current_point in [X - 1, X, X + 1]:
            grid[int(cycle // 40)][current_point] = "#"
        cycle += 1
        if cycle in stop_points:
            p1_total += X * cycle
        X += int(line[1])

print(f"Part 1: {p1_total}\nPart 2:")
["".join(x) for x in grid]
