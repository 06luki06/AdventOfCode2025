class Row:
    def __init__(self, left, mid, right):
        self.left = left
        self.mid = mid
        self.right = right

    def __str__(self):
        return f"{self.left}{self.mid}{self.right}"

class Grid:
    def __init__(self, top_row: Row, middle_row: Row, bottom_row: Row):
        self.top_row = top_row
        self.middle_row = middle_row
        self.bottom_row = bottom_row
    
    def has_less_than_x_neighbours(self,  x: int) -> bool:
        neighbours = str(self)
        paper_towels = neighbours.count('@')
        if self.middle_row.mid == '@':
            paper_towels -= 1
        return paper_towels < x
        
    def __str__(self):
        return self.top_row.__str__() + self.middle_row.__str__() + self.bottom_row.__str__()
    
with open('./inputs/04_input.txt', 'r') as file:
    lines = [list(line) for line in file.read().strip().split('\n')]

line_amounts = len(lines)
line_length = len(lines[0])
lines.insert(0, ['.'] * line_length)
lines.append(['.'] * line_length)

paper_rolls = 0

for line in lines:
    line.insert(0, '.')
    line.append('.')

for i in range(1, len(lines) - 1):
    line = lines[i]

    for j in range(1, len(lines[0]) - 1):
        if(lines[i][j] == '.'):
            continue

        top_row = Row(lines[i-1][j-1], lines[i-1][j], lines[i-1][j+1])
        middle_row = Row(lines[i][j-1], lines[i][j], lines[i][j+1])
        bottom_row = Row(lines[i+1][j-1], lines[i+1][j], lines[i+1][j+1])
        grid = Grid(top_row, middle_row, bottom_row)
        if grid.has_less_than_x_neighbours(4):
            paper_rolls += 1

print(paper_rolls)
