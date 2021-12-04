n = open("../day04/day04.txt", "r").read().split("\n\n")
n = [i.replace("\n", " ") for i in n]
output = len(n)
for i in n:
    necessary = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": 0, "hcl": 0, "ecl": 0, "pid": 0}
    h = i.split()
    for j in h:
        cat = j.split(":")[0]
        val = j.split(":")[1]
        if cat == "byr" and 1920 <= int(val) <= 2002:
            necessary[cat] = 1
        elif cat == "iyr" and 2010 <= int(val) <= 2020:
            necessary[cat] = 1
        elif cat == "eyr" and 2020 <= int(val) <= 2030:
            necessary[cat] = 1
        elif cat == "hgt":
            unit = val[len(val)-2:]
            num = val[:len(val)-2]
            if not num.isnumeric():
                continue
            num = int(num)
            if (unit == "cm" and 150 <= num <= 193) or (unit == "in" and 59 <= num <= 76):
                necessary[cat] = 1
        elif cat == "hcl" and val[0] == "#":
            isValid = True
            for h in val[1:]:
                if h not in "0123456789abcdef":
                    isValid = False
            if isValid:
                necessary[cat] = 1
        elif cat == "ecl":
            isValid = True
            if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                necessary[cat] = 1
        elif cat == "pid":
            if val.isnumeric() and len(val) == 9:
                necessary[cat] = 1
    for j in necessary:
        if necessary[j] == 0:
            output -= 1
            break
print(output)
