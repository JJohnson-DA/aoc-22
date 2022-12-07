#%%
# first guess 1038055

with open("../data/d7.txt", "r") as f:
    output = [x.rstrip() for x in f.readlines()]

structure = {}
current_dir = []

for line in output:
    # print(line)
    # print(f'start: {current_dir}')
    # print()
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

    # print(f'end: {current_dir}')
    # for dir in current_dir:
    #     print(f'{dir} = {structure[dir]}')
    # print('\n')

total = 0
for dir, size in structure.items():
    # print(dir, size)
    # print(size)
    if size <= 100000:
        total += size
        print(dir, size)

# %%
