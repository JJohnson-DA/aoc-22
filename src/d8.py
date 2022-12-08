#%%
# first guess 862, second 1237
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
print(p1_total)

#%% ---- Part 2 ----------------------------------------------------------------
with open("../data/d8.txt", "r") as f:
    grid = [x.rstrip() for x in f.readlines()]

grid_T = ["".join([row[i] for row in grid]) for i in range(len(grid[0]))]

# find_optimal_view():
max_view = 0
# Iterate over each tree
for row in range(len(grid)):
    for col in range(len(grid[0])):
        # Set counter objects for tree
        left, right, top, bottom = 0, 0, 0, 0
        # iterate going left checking if trees are equal or higher, keeping a counter for
        # ones that are not, stop if you get to an edge
        if col != 0:
            left_check_complete = False
            for i in list(range(-1, col))[::-1]:
                if grid[row][i] > grid[row][col] or left_check_complete:
                    pass
                elif grid[row][i] == grid[row][col]:
                    left_check_complete = True
                    left += 1
                else:
                    left += 1
        # Check Right
        if col != len(grid[0]) - 1:
            right_check_complete = False
            for i in list(range(col + 1, len(grid[0]))):
                if grid[row][i] > grid[row][col] or right_check_complete:
                    pass
                elif grid[row][i] == grid[row][col]:
                    right_check_complete = True
                    right += 1
                else:
                    right += 1
        # Check Top
        if col != 0:
            top_check_complete = False
            for i in list(range(-1, col))[::-1]:
                if grid_T[col][i] > grid_T[col][row] or top_check_complete:
                    pass
                elif grid_T[col][i] == grid_T[col][row]:
                    top_check_complete = True
                    top += 1
                else:
                    top += 1
        # Check Bottom
        if col != len(grid_T[0]) - 1:
            bottom_check_complete = False
            for i in list(range(col + 1, len(grid_T[0]))):
                if grid_T[col][i] > grid_T[col][row] or bottom_check_complete:
                    pass
                elif grid_T[col][i] == grid_T[col][row]:
                    bottom_check_complete = True
                    bottom += 1
                else:
                    bottom += 1
        tree_score = left * right * bottom * top
        if tree_score > max_view:
            max_view = tree_score

# iterate going right checking if trees are equal or higher, keeping a counter for
# ones that are not, stop if you get to an edge

# Transpose data

# Repeat left and right search but keep counters for "top" and "bottom"

# Multiply scores and replace value in tracker or keep track of max?
