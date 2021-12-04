from copy import deepcopy as dc
n = open("../day16/day16.txt", "r").read().split("\n\n")
rules = {}
for i in n[0].split("\n"):
    rules[i.split(": ")[0]] = [i.split(": ")[1].split(" or ")[0].split("-")[0], i.split(": ")[1].split(" or ")[0].split("-")[1], i.split(": ")[1].split(" or ")[1].split("-")[0], i.split(": ")[1].split(" or ")[1].split("-")[1]]
my_ticket = n[1].split("\n")[1].split(",")
other_tickets = [i.split(",") for i in n[2].split("\n")[1:]]
ticket_scanning_error_rate = 0
valid = False
invalid_tickets = []
for i in range(len(other_tickets)):
    for j in other_tickets[i]:
        valid = False
        for k in rules:
            rule = rules[k]
            if int(rule[0]) <= int(j) <= int(rule[1]) or int(rule[2]) <= int(j) <= int(rule[3]):
                valid = True
                break
        if not valid:
            ticket_scanning_error_rate += int(j)
            if i not in invalid_tickets:
                invalid_tickets.append(i)
print("Puzzle 1: ", ticket_scanning_error_rate)
# Part 2:


def is_valid(number, rule_set):
    min1 = int(rule_set[0])
    min2 = int(rule_set[2])
    max1 = int(rule_set[1])
    max2 = int(rule_set[3])
    return (min1 <= int(number) <= max1) or (min2 <= int(number) <= max2)


def remove_item_from_candidates(dictionary, item):
    for v in dictionary:
        remove = False
        index = 0
        for g in range(len(dictionary[v])):
            if dictionary[v][g] == item:
                index = g
                remove = True
                break
        if remove:
            dictionary[v].pop(index)
    return dictionary


other_tickets_error_corrected = [other_tickets[i] for i in range(len(other_tickets)) if i not in invalid_tickets]
tickets_by_field = []
for i in range(len(other_tickets[0])):
    tickets_by_field.append([j[i] for j in other_tickets_error_corrected])
important_rules = dc(rules)
rules_candidates = {i: list() for i in range(len(tickets_by_field))}
field_works = False
for i in rules_candidates:
    for j in important_rules:
        field_works = True
        for k in tickets_by_field[i]:
            if not is_valid(k, important_rules[j]):
                field_works = False
                break
        if field_works:
            rules_candidates[i].append(j)
rules_candidates = dict(sorted(rules_candidates.items(), key=lambda v: len(v[1])))
t = dc(rules_candidates)
for i in t:
    if len(rules_candidates[i]) == 0:
        rules_candidates.pop(i)
del t
fields_final = {}
rc_copy = dc(rules_candidates)
while len(rules_candidates) > 0:
    for i in rc_copy:
        fields_final[i] = rules_candidates[i][0]
        rules_candidates = remove_item_from_candidates(rules_candidates, rules_candidates[i][0])
        rules_candidates.pop(i)
        rules_candidates = dict(sorted(rules_candidates.items(), key=lambda v: len(v[1])))
my_product = 1
for i in fields_final:
    if "departure" in fields_final[i]:
        my_product *= int(my_ticket[int(i)])
print("Puzzle 2: ", my_product)
