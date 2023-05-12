numbers = tuple([float(num) for num in input().split()])

occurrences = {}

for el in numbers:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1

for key, value in occurrences.items():
    print(f"{key} - {value} times")
