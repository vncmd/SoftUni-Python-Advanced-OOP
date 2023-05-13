longest_intersection = set()

n_data = int(input())
for _ in range(n_data):
    first_data, second_data = [el.split(",") for el in input().split("-")]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)
