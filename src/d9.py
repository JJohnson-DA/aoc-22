#%%
# 105 too low
with open("../data/d9.txt") as f:
    steps = [x.rstrip().split() for x in f.readlines()]

# Starting Coordinates
h, t = [0, 0], [0, 0]

# List to store positions of tail, will convert to set at end to count unique
coords = list()


def move_head(direction):
    if direction == "D":
        h[1] -= 1
    elif direction == "U":
        h[1] += 1
    elif direction == "L":
        h[0] -= 1
    else:
        h[0] += 1


def move_tail():
    # Points overlap
    if t == h:
        pass
    # Allowable Diagonal
    elif abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1:
        pass
    # h is to the side of t
    elif t[1] == h[1] and abs(h[0] - t[0]) > 1:
        if t[0] > h[0]:
            t[0] -= 1
        else:
            t[0] += 1
    # h is above or below t
    elif t[0] == h[0] and abs(h[1] - t[1]) > 1:
        if t[1] > h[1]:
            t[1] -= 1
        else:
            t[1] += 1
    # h is diagonal with two side steps
    elif abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) > 1:
        # h is bottom left
        if t[1] > h[1] and t[0] > h[0]:
            t[0] -= 1
            t[1] -= 1
        # h is top left
        elif t[1] > h[1] and t[0] < h[0]:
            t[0] += 1
            t[1] -= 1
        # h is top right
        elif t[1] < h[1] and t[0] < h[0]:
            t[0] += 1
            t[1] += 1
        # h is bottom right
        else:
            t[0] -= 1
            t[1] += 1
    # h is diagonal with two vertical steps
    elif abs(h[1] - t[1]) == 1 and abs(h[0] - t[0]) > 1:
        # h is bottom left
        if t[0] > h[0] and t[1] > h[1]:
            t[0] -= 1
            t[1] -= 1
        # h is top left
        elif t[0] > h[0] and t[1] < h[1]:
            t[0] += 1
            t[1] -= 1
        # h is top right
        elif t[0] < h[0] and t[1] < h[1]:
            t[0] += 1
            t[1] += 1
        # h is bottom right
        else:
            t[0] -= 1
            t[1] += 1


for order in steps:
    direction = order[0]
    movements = order[1]
    move_head(direction)
    move_tail()
    coords.append("".join([str(x) for x in t]))
print(len(set(coords)))
# %%
