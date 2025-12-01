from typing import Callable

LINES = lambda s: s.split("\n")
INTS = lambda s: list(map(int, s.split("\n")))

class AOC:
    def __init__(self, day: int, transform: Callable[[str], iter] = None):
        if transform is None:
            transform = LINES
        self.puzzle_input = transform(open(f"day_{day:02}/input.txt", "r").read())
        self.test_input = transform(open(f"day_{day:02}/test.txt", "r").read())

    def test(self, p1 = None, p2 = None):
        if p1 is None and p2 is None:
            return None
        out = [None, None]
        if p1:
            out[0] = p1(self.test_input)
        if p2:
            out[1] = p2(self.test_input)
        return tuple(out)

    def run(self, p1 = None, p2 = None):
        if p1 is None and p2 is None:
            return None
        out = [None, None]
        if p1:
            out[0] = p1(self.puzzle_input)
        if p2:
            out[1] = p2(self.puzzle_input)
        return tuple(out)