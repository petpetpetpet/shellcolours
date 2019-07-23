import sys
import os

def to_dec(hexstr):
    return int(hexstr, 16)


class ColourString:

    def __init__(self, hex_str):
        if len(hex_str) == 7:
            self.hex_str = hex_str[1:]

        if len(self.hex_str) != 6:
            raise Exception(f"Invalid colour string input: {hex_str}")

        self.r = to_dec(self.hex_str[:2])
        self.g = to_dec(self.hex_str[2:-2])
        self.b = to_dec(self.hex_str[-2:])

    def term_str(self):
        return f"[38;2;{c.r};{c.g};{c.b}m"

    def __repr__(self):
        return f"({self.r},{self.g},{self.b})"


inputfile = sys.argv[1]
print(f"Reading list of hex colours from: {inputfile}")

colourstrings = list()
with open(inputfile, "r") as i:
    for line in i:
        colourstr = line.rstrip("\r\n")
        colourstrings.append(colourstr)


for colourstr in colourstrings:
    c = ColourString(colourstr)
    print(f"\033[38;2;255;255;255m{c.term_str()}\033{c.term_str()} {colourstr}");
