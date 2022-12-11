#%%
import math


class Monkey:
    def __init__(self, text):
        lines = text.strip().split("\n")
        self.number = int(lines[0].split()[1][:-1])
        self.current_items = [int(x) for x in lines[1].split(":")[1].split(",")]
        self.operation_string = lines[2].split("=")[1].strip()
        self.test_string = f"new_item % {lines[3].split()[-1]}"
        self.true_throw = int(lines[4].split()[-1])
        self.false_throw = int(lines[5].split()[-1])
        self.inspected_items = 0

    def throw_to_monkey(self, old, true_monkey, false_monkey, worry_reduction=3):
        self.inspected_items += 1
        if worry_reduction == 3:
            new_item = eval(self.operation_string) // worry_reduction
        else:
            new_item = eval(self.operation_string) % worry_reduction
        if eval(self.test_string) == 0:
            true_monkey.receive_item(new_item)
        else:
            false_monkey.receive_item(new_item)
        self.current_items = self.current_items[1:]

    def receive_item(self, item):
        self.current_items.extend([item])


with open("../data/d11.txt", "r") as f:
    monkeys = [Monkey(x) for x in f.read().split("\n\n")]

# ---- Part 1 ----
for round in range(20):
    for monkey in monkeys:
        for old_item in monkey.current_items:
            monkey.throw_to_monkey(
                old=old_item,
                true_monkey=monkeys[monkey.true_throw],
                false_monkey=monkeys[monkey.false_throw],
            )

p1 = math.prod(sorted([monkey.inspected_items for monkey in monkeys])[-2:])

# ---- Part 2 ----
with open("../data/d11.txt", "r") as f:
    monkeys = [Monkey(x) for x in f.read().split("\n\n")]

lcm = math.prod(set(int(monkey.test_string.split()[-1]) for monkey in monkeys))

for round in range(10000):
    for monkey in monkeys:
        for old_item in monkey.current_items:
            monkey.throw_to_monkey(
                old=old_item,
                true_monkey=monkeys[monkey.true_throw],
                false_monkey=monkeys[monkey.false_throw],
                worry_reduction=lcm,
            )

p2 = math.prod(sorted([monkey.inspected_items for monkey in monkeys])[-2:])

# ---- Results ----
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
