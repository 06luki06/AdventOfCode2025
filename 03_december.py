from functools import reduce

# Monotonic Stack algorithm
def get_max_joltage(numbers, target_len):
    stack = []
    to_remove = len(numbers) - target_len
    
    for num in numbers:
        while to_remove > 0 and stack and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)
    
    return int("".join(map(str, stack[:target_len])))

with open('./inputs/03_input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

total_joltage = 0
for line in lines:
    numbers = [int(d) for d in line.strip()]
    total_joltage += get_max_joltage(numbers, 12)

print(total_joltage)
