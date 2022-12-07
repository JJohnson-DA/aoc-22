#%%
with open("../data/d7.txt", "r") as f:
    output = [x.rstrip() for x in f.readlines()]

structure = {}
current_dir = []

# ---- Part 1 ----
for line in output:
    size = 0
    # Remove a level from current directory
    if line.startswith("$ cd .."):
        current_dir.pop()
    # Reset current directory to home
    elif line.startswith("$ cd /"):
        current_dir = ["/"]
        if "/" not in structure:
            structure["/"] = 0
    # Append to current dir, and add to structure if needed
    elif line.startswith("$ cd"):
        dir = line.split()[-1]
        current_dir.append(dir)
        full_path = "/".join(current_dir)
        if full_path not in structure:
            structure[full_path] = 0
    # add file size to all directories in the current dir
    elif line[0].isdigit():
        size = int(line.split()[0])
        for i in range(1, len(current_dir) + 1):
            partial_path = "/".join(current_dir[:i])
            structure[partial_path] += size
p1_total = sum(x for x in structure.values() if x <= 100000)

# ---- Part 2 ----
need_to_delete = structure["/"] - 40000000

min_dir_size = min([size for size in structure.values() if size >= need_to_delete])


print(f"Part 1: {p1_total}")
print(f"Part 2: {min([size for size in structure.values() if size >= need_to_delete])}")
