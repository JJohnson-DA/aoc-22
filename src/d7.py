#%%
# first guess 1038055

with open("../data/d7.txt", "r") as f:
    output = [x.rstrip() for x in f.readlines()]

structure = {}
current_dir = []

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
    # Append to current directory, and add to structure if needed
    elif line.startswith("$ cd"):
        dir = line.split(" ")[-1]
        current_dir.append(dir)
        if dir not in structure:
            structure[dir] = 0
    # add file size to all directories in the current dir
    elif line[0].isdigit():
        size = int(line.split(" ")[0])
        for dir in current_dir:
            structure[dir] += size

total = sum(x for x in structure.values() if x <= 100000)
