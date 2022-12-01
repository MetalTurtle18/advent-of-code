from shutil import copytree

if __name__ == "__main__":
    day = int(input("What day is it? "))
    copytree("../2022/template", f"../2022/day_{day:02}")
