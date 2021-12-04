from modint import chinese_remainder
n = open("../day13/day13.txt", "r").read().split("\n")
earliest_timestamp = int(n[0])
bus_ids_part_one = n[1].replace("x,", "").split(",")
bus_next_times = []
for i in bus_ids_part_one:
    bus_next_times.append((earliest_timestamp // int(i) + 1) * int(i))
min_time = min(bus_next_times)
index = 0
for i in range(len(bus_next_times)):
    if bus_next_times[i] == min_time:
        index = i
        break
print("Puzzle 1: " + str(int(bus_ids_part_one[index]) * (bus_next_times[index] - int(earliest_timestamp))))
# Part 2:
bus_ids = n[1].split(",")
print("Puzzle 2: " + str(chinese_remainder([int(bus_ids[i]) for i in range(len(bus_ids)) if not bus_ids[i] == "x"],
                                           [int(bus_ids[i])-i for i in range(len(bus_ids)) if not bus_ids[i] == "x"])))
