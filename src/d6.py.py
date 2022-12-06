#%%
with open("../data/d6.txt", "r") as f:
    code = f.read()


def search(length):
    for i in range(length, len(code)):
        if len(set(code[i : i + length])) == length:
            return i + length


print(f"Part 1: {search(4)}\nPart 2: {search(14)}")
