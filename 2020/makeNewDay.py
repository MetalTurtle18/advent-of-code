from os import mkdir
day = input("Which day is it?\n")
mkdir("day" + day)
python_file = open("day" + day + "/code" + day + ".py", "w")
python_file.write("p_in = open(\"input" + day + ".txt\", \"r\").read().split(\"\\n\")")
python_file.close()
input_file = open("day" + day + "/input" + day + ".txt", "w")
input_file.close()
test_input_file = open("day" + day + "/test" + day + ".txt", "w")
test_input_file.close()
