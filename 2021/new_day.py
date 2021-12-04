from shutil import copytree

if __name__ == "__main__":
    day = int(input("What day is it? "))
    copytree("2021/template", f"2021/day_{day:02}")
