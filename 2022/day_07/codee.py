class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.directories = {}
        self.files = {}
        self.parent = parent

    def __str__(self):
        output = '- ' + self.name + ' (dir, size=' + str(self.size) + ')'
        for f in self.files:
            output += '\n  - ' + f + ' (file, size=' + str(self.files[f]) + ')'
        for d in self.directories:
            output += '\n  ' + str(self.directories[d]).replace('\n', '\n  ')

        return output

    @property
    def size(self):
        return sum([f for f in self.files.values()] + [d.size for d in self.directories.values()])


def create_file_system(data) -> Directory:
    file_system = Directory("/")
    current_dir: Directory = file_system
    for line in data:
        if line.startswith('$'):  # command
            command, *args = line.split(' ')[1:]
            if command == 'cd':
                directory = args[0]
                if directory == '..':
                    current_dir = current_dir.parent
                    continue
                elif directory == '/':
                    current_dir = file_system
                    continue
                elif directory not in current_dir.directories:
                    current_dir.directories[directory] = Directory(directory, current_dir)
                current_dir = current_dir.directories[directory]
        else:  # not command; in ls listing? I think?
            s, name = line.split(' ')
            if s == 'dir':  # directory
                if name not in current_dir.directories:
                    current_dir.directories[name] = Directory(name, current_dir)
            else:  # file
                current_dir.files[name] = int(s)

    return file_system


def part1_rec(fs, total):
    for _d in fs.directories:
        total += part1_rec(d := fs.directories[_d], 0)
        if d.size <= 100000:
            total += d.size
    return total

def part1(data):
    fs = create_file_system(data)

    return part1_rec(fs, 0)


def part2(data):
    return data[0]


puzzle_input = open("input.txt", "r").read().split("\n")
test_input = open("test.txt", "r").read().split("\n")

if __name__ == "__main__":
    print("TEST:")
    print(f"Part 1: {part1(test_input)}")
    # print(f"Part 2: {part2(test_input)}")
    print("MAIN:")
    print(f"Part 1: {part1(puzzle_input)}")
    # print(f"Part 2: {part2(puzzle_input)}")
