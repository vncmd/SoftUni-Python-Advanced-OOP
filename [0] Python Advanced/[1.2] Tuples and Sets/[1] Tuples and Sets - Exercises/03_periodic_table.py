elements = set()

data = int(input())

for _ in range(data):
    current_element = input().split()
    for el in current_element:
        elements.add(el)

print(*elements, sep="\n")
