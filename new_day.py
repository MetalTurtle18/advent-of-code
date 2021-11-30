from shutil import copytree

if __name__ == "__main__":
    day = int(input("What day is it? "))
    copytree("template", f"day_{day:02}")
