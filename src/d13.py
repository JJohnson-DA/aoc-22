#%%
with open("../data/d13.txt", "r") as f:
    pairs = [[eval(y) for y in x.split("\n")] for x in f.read().split("\n\n")]


# Need some kind of function that handles each comparison option

# Needs to be nested somehow. Maybe a function that calls itself within it?

# For pair in pairs: pass left and right into function

# def compare(left, right):
# If both values are integers:
# If left > right: return True
# If left < right: return False
# If left == right: do nothing

# If both values are lists:
# Iterate over lists and run compare() on each pair of items.

# If one is int, and one is list, convert int to list and then feed into comparison
# function recursively --> return compare()
