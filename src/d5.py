#%%
from re import findall

crate_map_2 = [
    [],
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"],
]

with open("../data/d5.txt", "r") as f:
    quantity, origin, destination = [], [], []
    crates_raw = []
    first_line = True
    for line in f.readlines():
        if line == "":
            pass
        elif line[0] == "[" or first_line:
            crates_raw.append(line)
        elif line[0] == "m":
            digits = findall("\d+", line)
            quantity.append(int(digits[0]))
            origin.append(int(digits[1]))
            destination.append(int(digits[2]))
        first_line = False

    # Parse Raw Crates
    num_stacks = int(len(crates_raw[0]) / 4)
    stacks = [[] for i in range(num_stacks + 1)]
    for i in range(len(crates_raw)):
        lb, ub = 0, 4
        for j in range(1, num_stacks + 1):
            segment = crates_raw[i][lb:ub]
            letter = findall("\w", segment)
            if len(letter) != 0:
                stacks[j].extend(letter)
            lb += 4
            ub += 4
    for i in range(len(stacks)):
        stacks[i].reverse()

    for i in range(len(quantity)):
        temp_list = []
        for m in range(quantity[i]):
            # ---- Part 1 ----
            stacks[destination[i]].append(stacks[origin[i]].pop())
            # ---- Part 2 ----
            temp_list.append(crate_map_2[origin[i]].pop())
        temp_list.reverse()
        crate_map_2[destination[i]].extend(temp_list)
