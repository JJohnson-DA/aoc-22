#%%
score_dict = {
    "ax": 4,
    "ay": 8,
    "az": 3,
    "bx": 1,
    "by": 5,
    "bz": 9,
    "cx": 7,
    "cy": 2,
    "cz": 6,
}
choice_scores = {"x": 1, "y": 2, "z": 3}
outcome_scores = {"x": 0, "y": 3, "z": 6}
strategy = {
    "a": {"x": "z", "y": "x", "z": "y"},
    "b": {"x": "x", "y": "y", "z": "z"},
    "c": {"x": "y", "y": "z", "z": "x"},
}

with open("../data/d2.txt", "r") as f:
    part_1_score = 0
    part_2_score = 0
    for line in f.readlines():
        code = line.lower().replace(" ", "").strip()
        part_1_score += score_dict[code]
        choice = strategy[code[0]][code[1]]
        temp_score = choice_scores[choice] + outcome_scores[code[1]]
        part_2_score += temp_score

print(f'Part 1: {part_1_score}\nPart 2: {part_2_score}')
