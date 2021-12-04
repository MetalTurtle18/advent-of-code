n = open("../day05/day05.txt", "r").read().split("\n")
output = 0
seat_ids = []
for i in n:
    row_code = i[:7]
    column_code = i[7:]
    row = [i for i in range(128)]
    column = [i for i in range(8)]
    for j in row_code:
        if j == "F":
            row = row[:len(row) // 2]
        elif j == "B":
            row = row[len(row) // 2:]
    for j in column_code:
        if j == "R":
            column = column[len(column) // 2:]
        elif j == "L":
            column = column[:len(column) // 2]
    seat_id = row[0] * 8 + column[0]
    seat_ids.append(seat_id)
seat_ids.sort(reverse=True)
for i in range(len(seat_ids)):
    if not seat_ids[i] == seat_ids[i+1] + 1:
        print("Puzzle 1: " + str(seat_ids[0]) + "\nPuzzle 2: " + str(seat_ids[i]-1))
        break
