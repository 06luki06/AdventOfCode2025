from functools import reduce
import time

class ID:
    def __init__(self, id_value: str):
        self.first_part = id_value.split('-')[0]
        self.second_part = id_value.split('-')[1]
    
    def get_range_with_repeating_digits(self):
        ranges = list(range(int(self.first_part), int(self.second_part) + 1))
        repeating = []
        for number in ranges:
            str_num = str(number)

            for i in range(1, len(str_num) + 1):
                block_size = i

                blocks = [str_num[j:j + block_size] for j in range(0, len(str_num), block_size)]

                equals = True
                for block in blocks:
                    if block != blocks[0]:
                        equals = False
                        break
                if equals and len(blocks) > 1:
                    repeating.append(number)
                    break

        return reduce(lambda a, b: a + b, repeating, 0)

    def __str__(self):
        return f"First Part: {self.first_part}, Second Part: {self.second_part}"
    
with open('./inputs/02_input.txt', 'r') as file:
    ids = [ID(line) for line in file.read().strip().split(',')]

print(reduce(lambda a, b: a + b.get_range_with_repeating_digits(), ids, 0))