#%%
with open("../data/d6.txt", "r") as f:
    code = f.read()


def search(length):
    lb, ub = 0, length
    for i in range(len(code)):
        if len(set(code[lb:ub])) == length:
            return ub
        lb += 1
        ub += 1


print(f"Part 1: {search(4)}\nPart 2: {search(14)}")
