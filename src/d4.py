#%%
with open("../data/d4.txt", "r") as f:
    p1_total = 0
    p2_total = 0
    for pair in f.readlines():
        # ---- Part 1 ----
        e1 = pair.split(",")[0].split("-")
        e2 = pair.split(",")[1].split("-")
        e1_range = range(int(e2[0]), int(e2[1]) + 1)
        e2_range = range(int(e1[0]), int(e1[1]) + 1)
        overlap = set(e1_range) & set(e2_range)
        if len(overlap) in [len(e1_range), len(e2_range)]:
            p1_total += 1
        # ---- Part 2 ----
        if len(overlap) > 0:
            p2_total += 1

print(f"Part 1: {p1_total}\nPart 2: {p2_total}")
