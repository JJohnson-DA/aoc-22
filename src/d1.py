#%%
with open("../data/d1p1.txt", "r") as f:
    totals, current = [], 0
    for line in f.readlines():
        if line != "\n":
            current += int(line)
        else:
            totals.append(current)
            current = 0
    sorted_totals = sorted(totals)

print(f"1st: {sorted_totals[-1]}\nTop 3: {sum(sorted_totals[-3:])}")
