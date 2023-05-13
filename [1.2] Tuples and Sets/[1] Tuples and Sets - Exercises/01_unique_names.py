names_count = int(input())
names = set()

for _ in range(names_count):
    data_names = input()
    names.add(data_names)

print(*names, sep="\n")
