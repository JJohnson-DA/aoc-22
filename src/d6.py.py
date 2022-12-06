#%%
with open("../data/d6.txt", "r") as f:
    code = f.read()


def find_marker(length: str):
    """
    Finds index in a string where the previous "length" characters
    are all unique.
    """
    for i in range(length, len(code)):
        if len(set(code[i : i + length])) == length:
            return i + length


print(f"Part 1: {find_marker(4)}\nPart 2: {find_marker(14)}")
