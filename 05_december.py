class IDs:
    def __init__(self, id_range):
        parts = id_range.split("-")
        self.min_id = int(parts[0])
        self.max_id = int(parts[1])

    def __contains__(self, id):
        return self.min_id <= id <= self.max_id

with open('./inputs/05_input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

ids = []
remaining_lines = lines.copy()
for line in lines:
    if(line) == '':
        remaining_lines.remove(line)
        break
    ids.append(IDs(line))
    remaining_lines.remove(line)

valid_ids = []

for val_str in remaining_lines:
        current_id = int(val_str)
        for id_range in ids:
            if current_id in id_range:
                valid_ids.append(val_str)
                break

print(len(set(valid_ids)))
    