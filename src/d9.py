#%%
with open("../data/d9.txt") as f:
    steps = [x.rstrip().split() for x in f.readlines()]

# List to store positions of tail, will convert to set at end to count unique
p1_coords, p2_coords = [], []


def move_head(head):
    if direction == "D":
        head[1] -= 1
    elif direction == "U":
        head[1] += 1
    elif direction == "L":
        head[0] -= 1
    else:
        head[0] += 1


def move_tail(head, tail):
    offset_x = head[0] - tail[0]
    offset_y = head[1] - tail[1]
    # Allowable Diagonal or overlapping
    if abs(offset_x) <= 1 and abs(offset_y) <= 1:
        pass
    # Vertical offset
    elif abs(offset_y) > 1 and offset_x == 0:
        tail[1] += offset_y / abs(offset_y)
    # Horizontal offset
    elif offset_y == 0 and abs(offset_x) > 1:
        tail[0] += offset_x / abs(offset_x)
    # Non-allowable diagonal, increment both by 1 in offset direction
    else:
        tail[0] += offset_x / abs(offset_x)
        tail[1] += offset_y / abs(offset_y)


knots = [[0, 0] for i in range(10)]

for step in steps:
    direction = step[0]
    movements = int(step[1])
    for i in range(movements):
        move_head(knots[0])
        for i in range(1, len(knots)):
            move_tail(knots[i - 1], knots[i])
            p1_coords.append(",".join([str(int(x)) for x in knots[1]]))
            p2_coords.append(",".join([str(int(x)) for x in knots[-1]]))

print(f"Part 1: {len(set(p1_coords))}\nPart 2: {len(set(p2_coords))}")
