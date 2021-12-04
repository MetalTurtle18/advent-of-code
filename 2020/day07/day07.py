from copy import deepcopy as dc


def check_for_others(input_dictionary):
    output_dict = input_dictionary.copy()
    for r in input_dictionary:
        for y in input_dictionary[r]:
            if y in holds_gold:
                holds_gold.append(r)
                output_dict.pop(r)
                break
    return output_dict


n = open("../day07/day07.txt", "r").read().split("\n")
bags_dict = {}
bags_dict_two = {}
holds_gold = []
for bag_rule in n:
    bag, holds = bag_rule.split(" contain ")
    bag = bag.replace("bags", "")
    bag = bag.replace(" ", "")
    holds = holds.replace(".", "")
    for j in holds:
        if not j.isalpha() and not j == ",":
            holds = holds.replace(j, "")
    holds = holds.replace("bags", "")
    holds = holds.replace("bag", "")
    bags_dict[bag] = holds.split(",")
new_bags_dict = bags_dict.copy()
for bag_rule in bags_dict:
    for j in bags_dict[bag_rule]:
        if j == "shinygold":
            holds_gold.append(bag_rule)
            new_bags_dict.pop(bag_rule)
            break
running_dict = new_bags_dict.copy()
for bag_rule in range(len(n)):
    running_dict = check_for_others(running_dict).copy()
print("Puzzle 1: " + str(len(holds_gold)))
# Part 2:


def count_bags(outer_bag):
    count = 0
    if len(bags_dict_two_two[outer_bag]) != 0:
        for inner_bag in bags_dict_two_two[outer_bag]:
            if inner_bag[0] == "n":
                return 0
            count += int(inner_bag[0])
            count += int(inner_bag[0]) * count_bags(inner_bag[1:])
        return count
    else:
        return 0


for bag_rule in n:
    bag, holds = bag_rule.split(" contain ")
    bag = bag.replace("bags", "")
    bag = bag.replace(" ", "")
    holds = holds.replace(".", "")
    holds = holds.replace(" ", "")
    holds = holds.replace("bags", "")
    holds = holds.replace("bag", "")
    bags_dict_two[bag] = holds.split(",")

bags_dict_two_two = dc(bags_dict_two)

for bag_rule in bags_dict_two:
    if bags_dict_two[bag_rule][0] == "n":
        bags_dict_two_two.pop(bag_rule)

print("Puzzle 2: " + str(count_bags("shinygold")))
