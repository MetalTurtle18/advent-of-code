from os import mkdir
from shutil import copyfile
from subprocess import run

if __name__ == "__main__":
    year = 2025
    day = int(input("What day puzzle? "))

    source_dir = f"../{year}/template"
    new_dir = f"../{year}/day_{day:02}"
    new_solution = f"../{year}/solution_{day:02}.py"

    mkdir(new_dir)
    copyfile(f"{source_dir}/input.txt", f"{new_dir}/input.txt")
    copyfile(f"{source_dir}/test.txt", f"{new_dir}/test.txt")

    with open(f"{source_dir}/solution.py.template") as f:
        content = f.read()

    with open(new_solution, "w") as f:
        f.write(content.replace("$DAY$", str(day)))

    run(["git", "add", new_solution])
