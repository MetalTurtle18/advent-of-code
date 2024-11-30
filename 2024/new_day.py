from shutil import copytree

if __name__ == "__main__":
    day = int(input("What day is it? "))
    copytree("../2024/template", f"../2024/day_{day:02}")
