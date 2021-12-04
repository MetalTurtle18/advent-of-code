n = open("../day02/day02.txt", "r").read().split("\n")
total = 0
for i in n:
    policy, password = i.split(": ")
    nums, char = policy.split(" ")
    first, last = nums.split("-")
    if (password[int(first)-1] == char and not password[int(last)-1] == char) or (not password[int(first)-1] == char and password[int(last)-1] == char):
        total += 1
print(total)
