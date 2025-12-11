class Code:
    def __init__(self, line):
        self.way = line[0]
        self.steps = int(line[1:])

    def __repr__(self):
        return f"Code(way='{self.way}', steps={self.steps})"

def calculate_new_position(start, code: Code):
    dial_size = 100
    hits = 0
    new_position = 0

    if code.way == 'L':
        target = start - code.steps
        hits = ((start - 1) // dial_size) - ((target - 1) // dial_size)
        new_position = target % dial_size
    elif code.way == 'R':
        target = start + code.steps
        hits = (target // dial_size) - (start // dial_size)
        new_position = target % dial_size

    return new_position, hits

with open('./inputs/01_input.txt', 'r') as file:
    lines = [line.strip() for line in file]

codes = [Code(line) for line in lines]

dialStart = 50
total_hits = 0

for code in codes:
    dialStart, hits = calculate_new_position(dialStart, code)
    total_hits += hits

print(f"Final sum: {total_hits}")