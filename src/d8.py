#%%
import numpy as np

with open("../data/d8.txt", "r") as f:
    grid = [x.rstrip() for x in f.readlines()]

# ---- Part 1 ------------------------------------------------------------------
tracker = np.zeros((len(grid), len(grid[0])))
# make perimiter visible
tracker[0], tracker[-1] = 1, 1
for i in range(len(tracker)):
    tracker[i][0], tracker[i][-1] = 1, 1


def check_horizontal():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid) - 1:
                pass
            else:
                left = max(grid[row][:col]) < grid[row][col]
                right = max(grid[row][col + 1 :]) < grid[row][col]
                if left or right:
                    tracker[row][col] = 1


def check_vertical():
    for row in range(len(grid_T)):
        for col in range(len(grid_T[0])):
            if row == 0 or col == 0 or row == len(grid_T) - 1 or col == len(grid_T) - 1:
                pass
            else:
                left = max(grid_T[row][:col]) < grid_T[row][col]
                right = max(grid_T[row][col + 1 :]) < grid_T[row][col]
                if left or right:
                    tracker_T[row][col] = 1


check_horizontal()
grid_T = ["".join([row[i] for row in grid]) for i in range(len(grid[0]))]
tracker_T = [[row[i] for row in tracker] for i in range(len(tracker[0]))]
check_vertical()

p1_total = 0
for i in range(len(tracker_T)):
    p1_total += sum(tracker_T[i])
print(f"Part 1: {p1_total}")

# ---- Part 2 ------------------------------------------------------------------
with open("../data/d8.txt", "r") as f:
    grid = [x.rstrip() for x in f.readlines()]


def score_tree(tree, search_space):
    score = 0
    cleared = False
    for search in search_space:
        if cleared == True:
            pass
        elif search >= tree:
            cleared = True
            score += 1
        else:
            score += 1
    return score


max_view = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        current_tree = grid[row][col]

        left_check = [grid[row][i] for i in list(range(0, col))[::-1]]
        left = score_tree(current_tree, left_check)

        right_check = [grid[row][i] for i in list(range(col + 1, len(grid[0])))]
        right = score_tree(current_tree, right_check)

        top_check = [grid[i][col] for i in list(range(0, row))[::-1]]
        top = score_tree(current_tree, top_check)

        bottom_check = [grid[i][col] for i in list(range(row + 1, len(grid)))]
        bottom = score_tree(current_tree, bottom_check)

        tree_score = left * right * bottom * top
        max_view = max(max_view, tree_score)

print(f"Part 2: {max_view}")
# %%
