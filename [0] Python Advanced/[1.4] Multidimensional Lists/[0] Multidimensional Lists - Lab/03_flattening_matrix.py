row = int(input())

flatted_data = []

for _ in range(row):
    current_list = [int(el) for el in input().split(", ")]
    flatted_data.extend(current_list)

print(flatted_data)
