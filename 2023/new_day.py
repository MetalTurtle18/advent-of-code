from shutil import copytree

if __name__ == "__main__":
    day = int(input("What day is it? "))
    copytree("../2023/template", f"../2023/day_{day:02}")
