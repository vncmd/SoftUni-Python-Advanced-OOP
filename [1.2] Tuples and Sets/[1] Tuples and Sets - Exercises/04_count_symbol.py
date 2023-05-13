data = input()

for letter in sorted(set(data)):
    print(f"{letter}: {data.count(letter)} time/s")


# Different solution:

# occ = {}
#
# data = input()
# for letter in data:
#     occ[letter] = occ.get(letter, 0) + 1
#
# for letter, times in sorted(occ.items()):
#     print(f"{letter}: {times} time/s")
