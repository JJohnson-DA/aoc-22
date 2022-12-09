#%%
with open("../data/d8.txt", "r") as f:
    grid = [x.rstrip() for x in f.readlines()]


def score_tree(tree, search_space):
    score = 0
    visible = True
    cleared = False
    for search in search_space:
        if cleared == True:
            pass
        elif search >= tree:
            cleared = True
            visible = False
            score += 1
        else:
            score += 1
    return score, visible


max_view, vis_count = 0, 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        current_tree = grid[row][col]

        left_check = [grid[row][i] for i in list(range(0, col))[::-1]]
        left, l_vis = score_tree(current_tree, left_check)

        right_check = [grid[row][i] for i in list(range(col + 1, len(grid[0])))]
        right, r_vis = score_tree(current_tree, right_check)

        top_check = [grid[i][col] for i in list(range(0, row))[::-1]]
        top, t_vis = score_tree(current_tree, top_check)

        bottom_check = [grid[i][col] for i in list(range(row + 1, len(grid)))]
        bottom, b_vis = score_tree(current_tree, bottom_check)

        tree_score = left * right * bottom * top
        max_view = max(max_view, tree_score)
        if l_vis or r_vis or t_vis or b_vis:
            vis_count += 1

print(f"Part 1: {vis_count}\nPart 2: {max_view}")
