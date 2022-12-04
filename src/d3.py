#%%
import string

letter_dict = dict(
    zip(string.ascii_letters, [i for i in range(1, len(string.ascii_letters) + 1)])
)

with open("../data/d3.txt", "r") as f:
    # ---- Part 1 ----
    p1_total = 0
    packs = []
    for line in f.readlines():
        pack = line.rstrip()
        packs.append(pack)
        half = int(len(pack) / 2)
        overlap = set(pack[:half]) & set(pack[half:])
        p1_total += letter_dict[overlap.pop()]

    # ---- Part 2 ----
    lb, ub, p2_total = 0, 3, 0
    for i in range(int(len(packs) / 3)):
        group = packs[lb:ub]
        overlap = set(group[0]) & set(group[1]) & set(group[2])
        p2_total += letter_dict[overlap.pop()]
        lb += 3
        ub += 3
