class Code:
    def __init__(self, line):
        self.way = line[0]
        self.steps = int(line[1:])

    def __repr__(self):
        return f"Code(way='{self.way}', steps={self.steps})"


with open('./inputs/01_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

codes = [Code(line) for line in lines]

dialStart = 50
hit0 = 0

for code in codes:
    if code.way == 'L':
        dialStart -= code.steps
    elif code.way == 'R':
        dialStart += code.steps

    dialStart = dialStart % 100
    if dialStart == 0:
        hit0 += 1

print(f"Number of times hit 0: {hit0}")
