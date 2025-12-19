from functools import reduce

with open('./inputs/03_input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

highest_numbers = []

for line in lines:
    numbers = [int(d) for d in str(line)]
    lineDict = {}
    for idx, number in enumerate(numbers):
        lineDict[idx] = number

    max_key = max(lineDict, key=lineDict.get)
    print("Max Key: {0} Value: {1}".format(max_key, lineDict[max_key]))
    max_key_first_position = True


    subset = {k: v for k, v in lineDict.items() if k > max_key}
    if subset == {}:
        subset = {k: v for k, v in lineDict.items() if k < max_key}
        max_key_first_position = False

    max_subset_key = max(subset, key=subset.get)
    print("Subset Max Key: {0} Value: {1}".format(max_subset_key, subset[max_subset_key]))

    if max_key_first_position:
        highest_numbers.append("".join([str(lineDict[max_key]), str(subset[max_subset_key])]))
    else:
        highest_numbers.append("".join([str(subset[max_subset_key]), str(lineDict[max_key])]))

print(reduce(lambda a, b: a + int(b), highest_numbers, 0))